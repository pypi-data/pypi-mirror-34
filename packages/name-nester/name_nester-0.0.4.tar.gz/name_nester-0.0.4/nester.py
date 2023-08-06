"""This is module of "nester.py" """
def print_lol(this_list,indent=False, level=0):
    """this function print contents of (nested)list
        to the stdout """
    for each_item in this_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1)
        else:
            if indent:
                for i in range(level):
                    print("\t", end='')
            print(each_item)
