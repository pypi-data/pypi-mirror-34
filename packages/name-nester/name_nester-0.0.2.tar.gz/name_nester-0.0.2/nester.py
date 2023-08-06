"""This is module of "nester.py" """
def print_lol(this_list, indent):
    """this function print contents of (nested)list
        to the stdout """
    for each_item in this_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent + 1)
        else:
            for i in range(indent):
                print("\t", end='')
            print(each_item)
