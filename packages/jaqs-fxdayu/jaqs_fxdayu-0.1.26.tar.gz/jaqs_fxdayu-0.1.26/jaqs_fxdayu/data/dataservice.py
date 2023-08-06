# noinspection PyUnresolvedReferences
from jaqs.data.dataservice import *
from jaqs.data.dataservice import RemoteDataService as OriginRemoteDataService
import os
import h5py
import json
import numpy as np
import pandas as pd
from jaqs.data.align import align
import jaqs.util as jutil
from jaqs_fxdayu.patch_util import auto_register_patch

class DataNotFoundError(Exception):
    pass

@auto_register_patch(parent_level=1)
class RemoteDataService(OriginRemoteDataService):
    def __init__(self):
        super(OriginRemoteDataService, self).__init__()
        self.data_api = None
        self._address = ""
        self._username = ""
        self._password = ""
        self._timeout = 60

        self._REPORT_DATE_FIELD_NAME = 'report_date'

    def query_industry_daily(self, symbol, start_date, end_date, type_='SW', level=1):
        """
        Get index components on each day during start_date and end_date.

        Parameters
        ----------
        symbol : str
            separated by ','
        start_date : int
        end_date : int
        type_ : {'SW', 'ZZ'}

        Returns
        -------
        res : pd.DataFrame
            index dates, columns symbols
            values are industry code

        """
        df_raw = self.query_industry_raw(symbol, type_=type_, level=level)

        dic_sec = jutil.group_df_to_dict(df_raw, by='symbol')
        dic_sec = {sec: df.sort_values(by='in_date', axis=0).reset_index()
                   for sec, df in dic_sec.items()}

        df_ann_tmp = pd.concat({sec: df.loc[:, 'in_date'] for sec, df in dic_sec.items()}, axis=1)
        df_value_tmp = pd.concat({sec: df.loc[:, 'industry{:d}_name'.format(level)]
                                  for sec, df in dic_sec.items()},
                                 axis=1)

        idx = np.unique(np.concatenate([df.index.values for df in dic_sec.values()]))
        symbol_arr = np.sort(symbol.split(','))
        df_ann = pd.DataFrame(index=idx, columns=symbol_arr, data=np.nan)
        df_ann.loc[df_ann_tmp.index, df_ann_tmp.columns] = df_ann_tmp
        df_value = pd.DataFrame(index=idx, columns=symbol_arr, data=np.nan)
        df_value.loc[df_value_tmp.index, df_value_tmp.columns] = df_value_tmp

        dates_arr = self.query_trade_dates(start_date, end_date)
        df_industry = align(df_value, df_ann, dates_arr)

        # TODO before industry classification is available, we assume they belong to their first group.
        df_industry = df_industry.fillna(method='bfill')
        df_industry = df_industry.astype(str)

        return df_industry

    def query_lb_fin_stat(self, type_, symbol, start_date, end_date, fields="", drop_dup_cols=None,
                          report_type='408001000'):
        """
        Helper function to call data_api.query with 'lb.income' more conveniently.

        Parameters
        ----------
        type_ : {'income', 'balance_sheet', 'cash_flow'}
        symbol : str
            separated by ','
        start_date : int
            Annoucement date in results will be no earlier than start_date
        end_date : int
            Annoucement date in results will be no later than start_date
        fields : str, optional
            separated by ',', default ""
        drop_dup_cols : list or tuple
            Whether drop duplicate entries according to drop_dup_cols.

        Returns
        -------
        df : pd.DataFrame
            index date, columns fields
        err_msg : str

        """
        view_map = {'income': 'lb.income', 'cash_flow': 'lb.cashFlow', 'balance_sheet': 'lb.balanceSheet',
                    'fin_indicator': 'lb.finIndicator'}
        view_name = view_map.get(type_, None)
        if view_name is None:
            raise NotImplementedError("type_ = {:s}".format(type_))

        dic_argument = {'symbol': symbol,
                        'start_date': start_date,
                        'end_date': end_date,
                        # 'update_flag': '0'
                        }
        if view_name != 'lb.finIndicator':
            dic_argument.update({'report_type': report_type})  # we do not use single quarter single there are zeros
            """
            408001000: joint
            408002000: joint (single quarter)
            """

        filter_argument = self._dic2url(dic_argument)  # 0 means first time, not update

        res, err_msg = self.query(view_name, fields=fields, filter=filter_argument,
                                  order_by=self._REPORT_DATE_FIELD_NAME)
        self._raise_error_if_msg(err_msg)

        # change data type
        try:
            cols = list(set.intersection({'ann_date', 'report_date'}, set(res.columns)))
            dic_dtype = {col: np.integer for col in cols}
            res = res.astype(dtype=dic_dtype)
        except:
            pass

        if drop_dup_cols is not None:
            res = res.sort_values(by=drop_dup_cols, axis=0)
            res = res.drop_duplicates(subset=drop_dup_cols, keep='first')

        return res, err_msg

    def predefined_fields(self):
        params, msg = self.query("help.predefine", "", "")
        if msg != "0,":
            raise Exception(msg)
        mapper = {}
        for api, param in params[params.ptype == "OUT"][["api", "param"]].values:
            mapper.setdefault(api, set()).add(param)
        return mapper


class LocalDataService(object):
    def __init__(self, fp):
        import sqlite3 as sql
        self.fp = os.path.abspath(fp)
        sql_path = os.path.join(fp, 'data.sqlite')

        #if not (os.path.exists(sql_path) and os.path.exists(h5_path)):
        if not os.path.exists(sql_path):
            raise FileNotFoundError("在{}目录下没有找到数据文件".format(fp))

        conn = sql.connect("file:%s?mode=ro" % sql_path, uri=True)
        self.conn = conn
        self.c = conn.cursor()

    def _get_attrs(self):
        dic = {}
        for root, dirs, files in os.walk(self.fp):
            name = root.split(self.fp)[-1][1:]
            for file_name in files:
                if file_name.endswith('.hd5'):
                    with h5py.File(os.path.join(root, (file_name))) as file:
                        if 'meta' in file.attrs:
                            value = json.loads(file.attrs['meta'])
                            dic[name + '_' + file_name[:-4]] = value
                        else:
                            dic[name + '_' + file_name[:-4]] = None

        sql = '''select * from "attrs";'''
        data = pd.read_sql(sql, self.conn)
        dic.update(data.set_index(['view']).to_dict(orient='index'))
        return dic

    def _get_last_updated_date(self):
        lst = []
        for path, fields in self._walk_path().items():
            view = path
            for i in fields:
                with h5py.File(os.path.join(self.fp, path, "%s.hd5" % i)) as file:
                    try:
                        lst.append({'view': view + '.' + i,
                                    'updated_date': file['date_flag'][-1][0]})
                    except:
                        pass
        d1 = pd.DataFrame(lst)
        d1['freq'] = '1d'

        sql = '''select * from "attrs";'''
        d2 = pd.read_sql(sql, self.conn)
        return pd.concat([d1, d2])

    @staticmethod
    def _dic2url(d):
        l = ['='.join([key, str(value)]) for key, value in d.items()]
        return '&'.join(l)

    def predefined_fields(self):
        params, msg = self.query("help.predefine", "", "")
        if msg != "0,":
            raise Exception(msg)
        mapper = {}
        for api, param in params[params.ptype == "OUT"][["api", "param"]].values:
            mapper.setdefault(api, set()).add(param)

        keys = os.listdir(self.fp)
        updater = {k: set([i[:-4] for i in os.listdir(os.path.join(self.fp, k)) if i.endswith('hd5')]) for k in keys if os.path.isfile(k)}
        mapper.update(updater)
        return mapper

    def query(self, view, filter, fields, **kwargs):
        if view == 'attrs':
            return pd.DataFrame(self._get_attrs()).T

        if view == 'updated_date':
            return self._get_last_updated_date()

        self.c.execute('''select * from sqlite_master where type="table";''')
        sql_tables = [i[1] for i in self.c.fetchall()]
        
        if fields == '':
            fields = '*' 
        
        if view in sql_tables:
            self.c.execute('''PRAGMA table_info([%s])''' % (view))
            cols = [i[1] for i in self.c.fetchall()]
            date_names = [i for i in cols if 'date' in i]
            if 'report_date' in date_names:
                date_name = 'report_date'
            elif len(date_names) == 0:
                date_name = None
            else:
                date_name = date_names[0]

            flt = filter.split('&')
            if flt[0] != '':  
                k,v = flt[0].split('=')
                if 'start_date' in flt[0]:
                    condition = '''SELECT %s FROM "%s" WHERE %s >= "%s"''' % (fields, view, date_name, v)
                elif 'end_date' in flt[0]:
                    condition = '''SELECT %s FROM "%s" WHERE %s <= "%s"''' % (fields, view, date_name, v)
                else:
                    condition = '''SELECT %s FROM "%s" WHERE %s = "%s"''' % (fields, view, k, v)
                
                for i in flt[1:]:
                    k,v = i.split('=')
                    if k == 'start_date':
                        condition += ''' AND %s >= "%s"''' % (date_name, v)
                    elif k == 'end_date':
                        condition += ''' AND %s <= "%s"''' % (date_name, v)
                    elif k == 'symbol':
                        symbols = '("' + '","'.join(v.split(',')) + '")'
                        condition += ''' AND %s IN %s''' % (k, symbols)
                    else:
                        condition += ''' AND %s = "%s"''' % (k, v)
                condition = condition + ';'
            
            else:
                condition = '''SELECT %s FROM "%s";''' % (fields, view)

            data_format = kwargs.get('data_format')
            if not data_format:
                data_format = 'pandas'

            if data_format == 'list':
                data = [i[0] for i in self.c.fetchall()]
                return data, '0, '
            elif data_format == 'pandas':
                data = pd.read_sql(condition, self.conn)
                return data, "0,"

        elif view == 'factor':      
            dic = {}
            for i in filter.split('&'):
                k,v = i.split('=')
                dic[k] = v
            return self.daily(dic['symbol'], dic['start'], dic['end'], fields, adjust_mode=None)
        
    def query_trade_dates(self,start_date, end_date):
        sql = '''SELECT * FROM "jz.secTradeCal" 
                 WHERE trade_date>=%s 
                 AND trade_date<=%s ''' % (start_date, end_date)

        data = pd.read_sql(sql, self.conn)
        return data['trade_date'].values

    def query_index_member(self, universe, start_date, end_date,data_format='list'):
        sql = '''SELECT * FROM "lb.indexCons"
                 WHERE index_code = "%s" ''' % (universe)

        data = pd.read_sql(sql, self.conn)
        
        symbols = [i for i in data['symbol'] if (i[0] == '0' or i[0] == '3' or i[0] == '6')]
        data = data[data['symbol'].isin(symbols)]
                
        data['out_date'][data['out_date'] == ''] = '20990101'
        data['in_date'] = data['in_date'].astype(int)
        data['out_date'] = data['out_date'].astype(int)
        data = data[(data['in_date'] <= end_date) & (data['out_date'] >= start_date)]
        if data_format == 'list':
            return list(set(data['symbol'].values))
        elif data_format == 'pandas':
            return data, "0,"

    def query_index_member_daily(self, index, start_date, end_date):
        """
        Get index components on each day during start_date and end_date.
        
        Parameters
        ----------
        index : str
            separated by ','
        start_date : int
        end_date : int

        Returns
        -------
        res : pd.DataFrame
            index dates, columns all securities that have ever been components,
            values are 0 (not in) or 1 (in)

        """
        df_io, err_msg = self.query_index_member(index, start_date, end_date, data_format='pandas')
        if err_msg != '0,':
            print(err_msg)
        
        def str2int(s):
            if isinstance(s, basestring):
                return int(s) if s else 99999999
            elif isinstance(s, (int, np.integer, float, np.float)):
                return s
            else:
                raise NotImplementedError("type s = {}".format(type(s)))
        df_io.loc[:, 'in_date'] = df_io.loc[:, 'in_date'].apply(str2int)
        df_io.loc[:, 'out_date'] = df_io.loc[:, 'out_date'].apply(str2int)
        
        # df_io.set_index('symbol', inplace=True)
        dates = self.query_trade_dates(start_date=start_date, end_date=end_date)

        dic = dict()
        gp = df_io.groupby(by='symbol')
        for sec, df in gp:
            mask = np.zeros_like(dates, dtype=np.integer)
            for idx, row in df.iterrows():
                bool_index = np.logical_and(dates > row['in_date'], dates < row['out_date'])
                mask[bool_index] = 1
            dic[sec] = mask
            
        res = pd.DataFrame(index=dates, data=dic)
        res.index.name = 'trade_date'
        
        return res
    
    def query_lb_fin_stat(self, type_, symbol, start_date, end_date, fields, drop_dup_cols=False):
        view_map = {'income': 'lb.income', 'cash_flow': 'lb.cashFlow', 'balance_sheet': 'lb.balanceSheet',
                    'fin_indicator': 'lb.finIndicator'}
        view_name = view_map.get(type_, None)
        if view_name is None:
            raise NotImplementedError("type_ = {:s}".format(type_))
        
        fld = fields
        symbols = '("' + '","'.join(symbol.split(',')) + '")'
        report_type = '408001000'

        if fields == "":
            fld = '*'
        
        if view_name == 'lb.finIndicator':
            sql = '''SELECT %s FROM "%s" 
              WHERE report_date>=%s 
              AND report_date<=%s 
              AND symbol IN %s ''' % (fld, view_name, start_date, end_date, symbols)
            
        else:
            sql = '''SELECT %s FROM "%s" 
              WHERE report_date>=%s 
              AND report_date<=%s 
              AND symbol IN %s 
              AND report_type = "%s"''' % (fld, view_name, start_date, end_date, symbols, report_type)

        data = pd.read_sql(sql, self.conn)
        if drop_dup_cols:
            data = data.drop_duplicates()
        data[data == ''] = np.NaN
        return data, "0,"

    def query_inst_info(self, symbol, fields, inst_type=""):
        symbol = symbol.split(',')
        symbols = '("' + '","'.join(symbol) + '")'
        
        self.c.execute('PRAGMA table_info([jz.instrumentInfo])')
        cols = [i[1] for i in self.c.fetchall()]
        if 'setlot' not in cols:
            fields = fields.replace('setlot', 'selllot')
        
        if inst_type == "":
            inst_type = "1"
        
        self.c.execute('''SELECT %s FROM "jz.instrumentInfo"
                      WHERE symbol IN %s 
                     AND inst_type = "%s"''' % (fields, symbols, inst_type))
        data = pd.DataFrame([list(i) for i in self.c.fetchall()], columns=fields.split(','))
        return data.set_index('symbol')   
    
    def query_lb_dailyindicator(self, symbol, start_date, end_date, fields=""):
        return self.daily(symbol, start_date, end_date, fields=fields, view='SecDailyIndicator')


    def query_adj_factor_daily(self, symbol_str, start_date, end_date, div=False):
        data, msg = self.daily(symbol_str, start_date, end_date,fields='adjust_factor')
        data = data.loc[:, ['trade_date', 'symbol', 'adjust_factor']]
        data = data.drop_duplicates()
        data = data.pivot_table(index='trade_date', columns='symbol', values='adjust_factor', aggfunc=np.mean)
        if div:
            pass
        return data

    def query_index_weights_range(self, universe, start_date, end_date):
        """
        Return all securities that have been in universe during start_date and end_date.
        
        Parameters
        ----------
        universe : str
            separated by ','
        start_date : int
        end_date : int

        Returns
        -------
        pd.DataFrame
        """
        universe = universe.split(',')
        if '000300.SH' in universe:
            universe.remove('000300.SH')
            universe.append('399300.SZ')
            
        if len(universe) == 1:
            universe = universe[0] 
            sql = '''SELECT * FROM "lb.indexWeightRange"
                      WHERE trade_date>=%s 
                      AND trade_date<=%s 
                      AND index_code = "%s" '''%(start_date, end_date, universe)
        else:
            universe = '("' + '","'.join(universe) + '")'
            sql = '''SELECT * FROM "lb.indexWeightRange"
                      WHERE trade_date>=%s 
                      AND trade_date<=%s 
                      AND index_code IN %s ''' % (start_date, end_date, universe)
            
        data = pd.read_sql(sql, self.conn).drop_duplicates()
        
        if len(data) > 0:
            # df_io = df_io.set_index('symbol')
            df_io = data.astype({'weight': float, 'trade_date': np.integer})
            df_io.loc[:, 'weight'] = df_io['weight'] / 100.
            df_io = df_io.pivot(index='trade_date', columns='symbol', values='weight')
            df_io = df_io.fillna(0.0)
            return df_io
        else:
            print('没有找到指数%s的权重数据' % self.universe)
            return data

    def query_index_weights_daily(self, index, start_date, end_date):
        """
        Return all securities that have been in index during start_date and end_date.
        
        Parameters
        ----------
        index : str
        start_date : int
        end_date : int

        Returns
        -------
        res : pd.DataFrame
            Index is trade_date, columns are symbols.

        """
        start_dt = jutil.convert_int_to_datetime(start_date)
        start_dt_extended = start_dt - pd.Timedelta(days=45)
        start_date_extended = jutil.convert_datetime_to_int(start_dt_extended)
        trade_dates = self.query_trade_dates(start_date_extended, end_date)
        
        df_weight_raw = self.query_index_weights_range(index, start_date=start_date_extended, end_date=end_date)
        res = df_weight_raw.reindex(index=trade_dates)
        res = res.fillna(method='ffill')
        res = res.loc[res.index >= start_date]
        res = res.loc[res.index <= end_date]
        
        mask_col = res.sum(axis=0) > 0
        res = res.loc[:, mask_col]
        
        return res

    def _walk_path(self, path=None):
        res = {}
        if not path:
            path = self.fp
        path = path[:-1] if path.endswith(os.path.sep) else path
        for a, b, c in os.walk(path):
            dr = a.replace(path, "")
            dr = dr[1:] if dr.startswith(os.path.sep) else dr
            depth = len(dr.split(os.path.sep))
            if not dr or depth != 1:
                continue
            lst = []
            for i in c:
                if '.hd5' in i:
                    lst.append(i[:-4].split(os.path.sep)[-1])
            res[dr] = lst
        return res

    def daily(self, symbol, start_date, end_date,
              fields="", adjust_mode=None, view='Stock_D'):

        if isinstance(fields, str):
            fields = fields.split(',')
        if isinstance(symbol, str):
            symbol = symbol.split(',')

        file_info = self._walk_path()
        exist_views = []
        for path, exists in file_info.items():
            if set(fields) & set(exists) == set(fields) and len(fields) > 0:
                exist_views.append(path)
        
        if "Stock_D" in set(exist_views):
            view = "Stock_D"
        elif exist_views:
            view = exist_views[0]

        if fields in [[''], []]:
            fields = file_info[view]
        exist_field = file_info[view]
        if view == 'Stock_D':
            basic_field = ['symbol', 'trade_date', 'freq']
        else:
            basic_field = ['symbol', 'trade_date']
        fields = list(set(fields + basic_field))
        fld = list(set(exist_field) & set(fields))
        
        need_dates = self.query_trade_dates(start_date, end_date)
        start = need_dates[0]
        end = need_dates[-1]

        if adjust_mode:
            fld = list(set(fld + ['adjust_factor']))

        def query_by_field(field):
            _dir = os.path.join(self.fp, view, field + '.hd5')
            with h5py.File(_dir) as file:
                try:
                    dset = file['data']
                    exist_symbol = file['symbol_flag'][:, 0].astype(str)
                    exist_dates = file['date_flag'][:, 0].astype(int)
                except:
                    raise DataNotFoundError('empty hdf5 file')

                if start not in exist_dates or end not in exist_dates:
                    raise ValueError('起止日期超限')

                _symbol = [x for x in symbol if x in exist_symbol]
                symbol_index = [np.where(exist_symbol == i)[0][0] for i in _symbol]
                symbol_index.sort()
                sorted_symbol = [exist_symbol[i] for i in symbol_index]

                start_index = np.where(exist_dates == start)[0][0]
                end_index = np.where(exist_dates == end)[0][0] + 1

                if symbol_index == []:
                    return None

                data = dset[start_index:end_index, symbol_index]

                if data.dtype not in ['float', 'float32', 'float16', 'int']:
                    data = data.astype(str)
                if field == 'trade_date' and data.dtype in ['float', 'float32', 'float16']:
                    data = data.astype(float).astype(int)
                cols_multi = pd.MultiIndex.from_product([[field], sorted_symbol], names=['fields', 'symbol'])
                return pd.DataFrame(columns=cols_multi, data=data)
        df = pd.concat([query_by_field(f) for f in fld], axis=1)
        df.index.name = 'trade_date'
        df = df.stack().reset_index(drop=True)

        if adjust_mode == 'post':
            if 'adjust_factor' not in df.columns:
                df['adjust_factor'] = 1
            else:
                df['adjust_factor'] = df['adjust_factor'].fillna(1)

            for f in list(set(df.columns) & set(['open', 'high', 'low', 'close', 'vwap'])):
                df[f] = df[f]*df['adjust_factor']
            df = df.dropna()

        if adjust_mode == 'pre':
            if 'adjust_factor' not in df.columns:
                df['adjust_factor'] = 1
            else:
                df['adjust_factor'] = df['adjust_factor'].fillna(1)

            for f in list(set(df.columns) & set(['open', 'high', 'low', 'close', 'vwap'])):
                df[f] = df[f]/df['adjust_factor']
            df = df.dropna()

        if ('adjust_factor' not in fields) and adjust_mode:
            df = df.drop(['adjust_factor'], axis=1)

        df = df.dropna(how='all')
        df = df[df['trade_date'] > 0]
        df = df.reset_index(drop=True)
        return df.sort_values(by=['symbol', 'trade_date']), "0,"
    
    def query_industry_raw(self, symbol_str, type_='ZZ', level=1):
        """
        Get daily industry of securities from ShenWanZhiShu or ZhongZhengZhiShu.
        
        Parameters
        ----------
        symbol_str : str
            separated by ','
        type_ : {'SW', 'ZZ'}
        level : {1, 2, 3, 4}
            Use which level of industry index classification.

        Returns
        -------
        df : pd.DataFrame

        """
        if type_ == 'SW':
            src = 'sw'
            if level not in [1, 2, 3, 4]:
                raise ValueError("For [SW], level must be one of {1, 2, 3, 4}")
        elif type_ == 'ZZ':
            src = 'zz'
            if level not in [1, 2, 3, 4]:
                raise ValueError("For [ZZ], level must be one of {1, 2}")
        else:
            raise ValueError("type_ must be one of SW of ZZ")
        
        symbol = symbol_str.split(',')
        symbols = '("' + '","'.join(symbol) + '")'
        sql = '''SELECT * FROM "lb.secIndustry"
                 WHERE symbol IN %s
                 AND industry_src == "%s" ''' % (symbols, src)

        df = pd.read_sql(sql, self.conn)
        df = df.astype(dtype={'in_date': np.integer,
                              # 'out_date': np.integer
                              })
        return df.drop_duplicates()

    def query_industry_daily(self, symbol, start_date, end_date, type_='SW', level=1):
        """
        Get index components on each day during start_date and end_date.
        
        Parameters
        ----------
        symbol : str
            separated by ','
        start_date : int
        end_date : int
        type_ : {'SW', 'ZZ'}

        Returns
        -------
        res : pd.DataFrame
            index dates, columns symbols
            values are industry code

        """
        def group_df_to_dict(df, by):
            gp = df.groupby(by=by)
            res = {key: value for key, value in gp}
            return res
        
        df_raw = self.query_industry_raw(symbol, type_=type_, level=level)
        
        dic_sec = group_df_to_dict(df_raw, by='symbol')
        dic_sec = {sec: df.sort_values(by='in_date', axis=0).reset_index()
                   for sec, df in dic_sec.items()}

        df_ann_tmp = pd.concat({sec: df.loc[:, 'in_date'] for sec, df in dic_sec.items()}, axis=1)
        df_value_tmp = pd.concat({sec: df.loc[:, 'industry{:d}_name'.format(level)]
                                  for sec, df in dic_sec.items()},
                                 axis=1)
        
        idx = np.unique(np.concatenate([df.index.values for df in dic_sec.values()]))
        symbol_arr = np.sort(symbol.split(','))
        df_ann = pd.DataFrame(index=idx, columns=symbol_arr, data=np.nan)
        df_ann.loc[df_ann_tmp.index, df_ann_tmp.columns] = df_ann_tmp
        df_value = pd.DataFrame(index=idx, columns=symbol_arr, data=np.nan)
        df_value.loc[df_value_tmp.index, df_value_tmp.columns] = df_value_tmp

        dates_arr = self.query_trade_dates(start_date, end_date)
        
        df_industry = align(df_value, df_ann, dates_arr)
        
        # TODO before industry classification is available, we assume they belong to their first group.
        df_industry = df_industry.fillna(method='bfill')
        df_industry = df_industry.astype(str)
        
        return df_industry

    def query_dividend(self, symbol, start_date, end_date):
        filter_argument = self._dic2url({'symbol': symbol,
                                         'start_date': start_date,
                                         'end_date': end_date})
        df, err_msg = self.query(view="lb.secDividend",
                                 fields="",
                                 filter=filter_argument,
                                 data_format='pandas')

        '''
        # df = df.set_index('exdiv_date').sort_index(axis=0)
        df = df.astype({'cash': float, 'cash_tax': float,
                        # 'bonus_list_date': np.integer,
                        # 'cashpay_date': np.integer,
                        'exdiv_date': np.integer,
                        'publish_date': np.integer,
                        'record_date': np.integer})
        '''
        return df, err_msg
