import pandas


class MySeries(pandas.Series):
    @property
    def _constructor(self):
        return MySeries

    @staticmethod
    def custom_series_function():
        return 'OK'


class MyDataFrame(pandas.DataFrame):
    """My custom data frame"""

    def __init__(self, *args, **kw):
        super(MyDataFrame, self).__init__(*args, **kw)

    @property
    def _constructor(self):
        return MyDataFrame

    _constructor_sliced = MySeries

    def filter_in_shenzhen(self, **args):
        """ filter the coordinates in shenzhen
        @author
        usage:
        >> df.filter_in_shenzhen(lon=lon_col_index, lat=lat_col_index)
        >> df.filter_in_shenzhen(lon=lon_col_name, lat=lat_col_name)
        """
        return self[(self.loc[:, args['lon']] > 113.73) & \
                    (self.loc[:, args['lon']] < 114.82) & \
                    (self.loc[:, args['lat']] > 22.43) & \
                    (self.loc[:, args['lat']] < 22.87)]