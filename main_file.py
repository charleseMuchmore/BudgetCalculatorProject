from regular_budget_plan import regular_budget_plan
from compromised_budget_plan import compromised_budget_plan

def nested_dict_pairs_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all key-value pairs of dict argument
    for key, value in dict_obj.items():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for pair in  nested_dict_pairs_iterator(value):
                yield (key, *pair)
        else:
            # If value is not dict type then yield the value
            yield (key, value)

def format_output(list_of_items_to_format):
    list_without_item_totals = []
    for item in list_of_items_to_format:
        sub_catagory = item[1]
        if sub_catagory != "total":
            list_without_item_totals.append(item)
    for item in list_without_item_totals:
        sub_catagory = item[1]
        dollar_amount = item[3]
        print(f"{sub_catagory}: ${dollar_amount}")



def calculate_budget(income, iterated_budget_plan):
    """ returns a list of lists with indexes 0-3, with index 3 being the actual dollars amount
    """
    temporary_list_of_items = []
    for item in iterated_budget_plan:
        item = list(item)
        percentage = float(item[2])
        income = float(income)
        amount_of_money = income * percentage
        item.append(amount_of_money)
        temporary_list_of_items.append(item)
        
        # if item[1] != "total":
        #     print(f"{item[0]}: \n\t-{item[1]}: ${item[3]}")
    format_output(temporary_list_of_items)
    return(temporary_list_of_items)





list_of_pairs = []
income_amount = input("Income Amount: $")
budget_type = input("Which budget plan, regular, or compromised? (r/c) ")
if budget_type == 'r':
    #Loop through all key-value pairs of a nested dictionary
    for pair in nested_dict_pairs_iterator(regular_budget_plan):
        list_of_pairs.append(pair)
    new_list = calculate_budget(income_amount, list_of_pairs)
elif budget_type == 'c':
    for pair in nested_dict_pairs_iterator(compromised_budget_plan):
        list_of_pairs.append(pair)
    new_list = calculate_budget(income_amount, list_of_pairs)




def check_budget_total(list_of_totals_where_index3_is_dollar_amount):
    total = 0
    for item in new_list:
        if item[1] != "total":
            total += item[3]
    print(f"total: {total}")
