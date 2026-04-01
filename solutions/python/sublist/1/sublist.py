SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def sublist(list_one, list_two):
    # If lists are identical
    if list_one == list_two:
        return EQUAL

    len_one, len_two = len(list_one), len(list_two)
    
    # Check if list_one is a sublist of list_two
    # We iterate through list_two to see if we can find list_one
    if len_one <= len_two:
        for i in range(len_two - len_one + 1):
            if list_two[i : i + len_one] == list_one:
                return SUBLIST
                
    # Check if list_one is a superlist of list_two
    # This is equivalent to checking if list_two is a sublist of list_one
    if len_two <= len_one:
        for i in range(len_one - len_two + 1):
            if list_one[i : i + len_two] == list_two:
                return SUPERLIST

    # If no match is found
    return UNEQUAL