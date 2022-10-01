import pandas

class PandasCommunicator:
    @staticmethod
    def read_csv(csv_filename):
        return pandas.read_csv(csv_filename)
        
    def iloc_dataframe(dataframe_object, input):
        return dataframe_object.iloc(input)

    def to_list(csv_filename):
        return pandas.to_list(csv_filename)

    def loc_dataframe(dataframe, list_of_column_names):
        return dataframe.loc[list_of_column_names]


    def iterate(dataframe):
        return dataframe.__iter__()

    def to_dict_dataframe(dataframe, parameter):
        return dataframe.to_dict(parameter)

    def columns(dataframe):
        return dataframe.columns

    def DataFrame(data, columns=None, dtype=None):
        return pandas.DataFrame(data, columns, dtype)

    def series_to_list(series):
        return pandas.Series.tolist(series)

    def Series(data):
        return pandas.Series(data)

    def rename(dataframe, mapper, axis):
        """mapper is dict that looks like this: {old_name1 : new_name1, old_name2 : new_name2}. Axis is either 0 or 1: 0=y, 1=x"""
        return dataframe.rename(mapper, axis=axis)

