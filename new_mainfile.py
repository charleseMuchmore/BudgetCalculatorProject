from pandas_communicator import PandasCommunicator



# print(f"\n{data}")\

# user_input = input("income amount: $")



dataframe = PandasCommunicator.read_csv("regular_budget_plan.csv") #data is a dataframe


list_of_column_names = [dataframe.category.name, dataframe.dollar_amount.name]
thing_to_print = PandasCommunicator.loc_dataframe(dataframe, list_of_column_names)
print(thing_to_print)



