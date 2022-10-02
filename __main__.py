from pandas_communicator import PandasCommunicator
from budget_calculator import BudgetCalculator
from dict_iterator import DictIterator
from user_display import UserDisplay
from title import Title

title = Title()

user_input_dollars_to_budget = int(title.print_title())
# user_input_dollars_to_budget = int(input("Income Amount: $"))
dataframe = PandasCommunicator.read_csv("regular_budget_plan.csv") #loads dataframe from csv
dataframe = BudgetCalculator.load_user_input_to_dataframe(dataframe, user_input_dollars_to_budget) #loads userinput into dataframe
dataframe = BudgetCalculator.calculate_all_budget_values(dataframe) #calculates all of the budget's values
category_dollaramount_df = UserDisplay.select_columns(dataframe, ('category', 'dollar_amount'), hide_indexes_yn='y') # selects what to show
print(category_dollaramount_df)
