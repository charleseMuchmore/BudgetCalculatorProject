from pandas_communicator import PandasCommunicator
from dict_iterator import DictIterator
class BudgetCalculator:

    def load_user_input_dollars_to_budget(dict_dataframe, user_input_dollars_to_budget):
        """"class method"""
        dollars_to_budget_index = DictIterator.search_dict_by_value(dict_dataframe['category'], 'dollars_to_budget') #returns 0
        dict_dataframe['dollar_amount'][dollars_to_budget_index] = user_input_dollars_to_budget
        return dict_dataframe

    def load_user_input_to_dataframe(dataframe, dollars_to_load):
        dict_dataframe = PandasCommunicator.to_dict_dataframe(dataframe, 'dict') #turns dataframe to dict
        updated_dict_dataframe = BudgetCalculator.load_user_input_dollars_to_budget(dict_dataframe, dollars_to_load) #loads dollars to budget
        dataframe = PandasCommunicator.DataFrame(updated_dict_dataframe) #goes back to dataframe
        return dataframe

    def calculate_dollar_amounts(dict_dataframe):
        """class method"""
        for row_num in range(len(dict_dataframe['category'])):#row_num can be used in conjunction with column name to find a value
            category = dict_dataframe['category'][row_num]#category of the row_num
            parent_category = dict_dataframe['parent_category'][row_num] #parent_category of the row_num
            percent_of_parent = dict_dataframe["percent_of_parent"][row_num] #percent of parent in that row
            parent_row_num = DictIterator.search_dict_by_value(dict_dataframe['category'], parent_category) #rownum for parent category
            parent_category_dollar_amount = dict_dataframe['dollar_amount'][parent_row_num] #dollar_amount for parent category
            new_dollar_amount =  parent_category_dollar_amount * percent_of_parent #calculates dollar amount
            new_dollar_amount = round(new_dollar_amount, 2) #rounds to the second decimal place
            dict_dataframe['dollar_amount'][row_num] = new_dollar_amount #puts the new number in the dictionary

    def calculate_all_budget_values(dataframe):
        dict_dataframe = PandasCommunicator.to_dict_dataframe(dataframe, 'dict') #turns the dataframe to a dict
        BudgetCalculator.calculate_dollar_amounts(dict_dataframe) #calculates dollar amounts
        dataframe = PandasCommunicator.DataFrame(dict_dataframe)#turns it back to a dataframe
        return dataframe