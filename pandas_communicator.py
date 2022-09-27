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
        return dataframe.loc[:, list_of_column_names]

    def iterate(dataframe):
        return dataframe.__iter__()

    def to_dict_dataframe(dataframe, parameter):
        return dataframe.to_dict(parameter)

    def columns(dataframe):
        return dataframe.columns

    def DataFrame(data_to_frame):
        return pandas.DataFrame(data_to_frame)