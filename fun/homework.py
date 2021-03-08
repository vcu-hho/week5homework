"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    greatest_value = max(incoming_list)

    return greatest_value


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    least_value = min(incoming_list)

    return least_value


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    try:
        total = sum(incoming_list)
        return total
    except:
        return 0


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    greatest = 0
    greatest_key = ""
    if incoming_dict == None or len(incoming_dict) == 0:
        return None
    else:
        for key in incoming_dict:
            for value in key:
                value_len = len(value)
                if value_len > greatest:
                    greatest = value_len
                    greatest_key = key
        return greatest_key