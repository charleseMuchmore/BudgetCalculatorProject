from pandas_communicator import PandasCommunicator
from budget_calculator import BudgetCalculator
from dict_iterator import DictIterator


user_input_dollars_to_budget = int(input("Income Amount: $"))

dataframe = PandasCommunicator.read_csv("regular_budget_plan.csv") #loads dataframe from csv
dataframe = BudgetCalculator.load_user_input_to_dataframe(dataframe, user_input_dollars_to_budget) #loads userinput into dataframe
dataframe = BudgetCalculator.calculate_all_budget_values(dataframe) #calculates all of the budget's values
print(dataframe)

# #unsorted logic to display only the category and dollar amount
# dict_dataframe = PandasCommunicator.to_dict_dataframe((dataframe), 'dict') #turn dataframe to dict
# new_dict_dataframe = dict_dataframe #make copy
# del new_dict_dataframe['parent_category'] #delete irrelevant info
# del new_dict_dataframe['percent_of_parent']
# new_dataframe = PandasCommunicator.DataFrame(new_dict_dataframe) #back to dataframe
# print(new_dataframe)




