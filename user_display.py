from pandas_communicator import PandasCommunicator


class UserDisplay:
    
    def display_row_info(dataframe, row_name):
        """Requires a dataframe and a str(row_name), returns a new dataframe containing the information from that row"""
        new_dataframe = PandasCommunicator.loc_dataframe(dataframe, row_name)
        return new_dataframe

    # def display_info_column(dataframe, column_name):
    #     """Requires a dataframe and a str(column_name), returns a new dataframe containing the information from that column"""

    def select_columns(dataframe, array_of_column_names, hide_indexes_yn=None):
        """array items must be string dtype, returns dataframe with only the given column names as its series"""
        listoseries = []
        for item in array_of_column_names:
            listoseries.append(dataframe[item])
        zipped = list(zip(*listoseries))
        listoseries = []
        for item in zipped:
            listoseries.append(PandasCommunicator.Series(item))        
        dataframe = PandasCommunicator.DataFrame(listoseries)
        dataframe_column_names = PandasCommunicator.columns(dataframe)
        dataframe_column_renamer = {}
        for num in range(0, len(array_of_column_names)):
            dataframe_column_renamer[num] = array_of_column_names[num]
        dataframe = PandasCommunicator.rename(dataframe, dataframe_column_renamer, axis=1)
        if hide_indexes_yn == 'y':
            blankIndex=[''] * len(dataframe)
            dataframe.index=blankIndex
        return(dataframe)


