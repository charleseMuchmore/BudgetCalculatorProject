
class DictIterator:

    def search_dict_by_value(dictionary, value):
        res = dict((v,k) for k,v in dictionary.items())
        return res[value]

    def check_column_for_item(dict_dataframe, column_to_check, item_to_check):
        for i in dict_dataframe[column_to_check]:
            if i == item_to_check:
                return dict_dataframe[column_to_check][i]

