"""Adding."""


def get_max_element(int_list):
    """
    Return the maximum element in the list.

    If the list is empty return None.
    :param int_list: List of integers
    :return: largest int
    """
    if len(int_list) == 0:
        return None

    return max(int_list)

    pass


def get_min_element(int_list):
    """
    Return the minimum element in list.

    If the list is empty return None.
    :param int_list: List of integers
    :return: Smallest int
    """
    if len(int_list) == 0:
        return None

    return min(int_list)
    pass


def sort_list(int_list):
    """
    Sort the list in descending order.

    :param int_list: List of integers
    :return: Sorted list of integers
    """
    return sorted([int_list], reverse=True)
    pass


def add_list_elements(int_list):
    """
    Create a new sorted list of the sums of minimum and maximum elements.

    Add together the minimum and maximum element of int_list and add that sum to a new list
    Repeat the process until all elements in the list are used, ignore the median number
    if the list contains uneven amount of elements.
    Sort the new list in descending order.
    This function must use get_min_element(), get_max_element() and sort_list() functions.
    :param int_list: List of integers
    :return: Integer list of sums sorted in descending order.
    """
    sort_list([int_list])
    new_int_list = []
    print(int_list)
    while get_max_element(int_list) is not None and get_min_element(int_list) is not None:
        if len(int_list) % 2 == 0 and len(int_list) > 1:
            uus1 = get_max_element(int_list)
            uus2 = get_min_element(int_list)
            print(int_list)
            uus3 = uus1 + uus2
            new_int_list.append(uus3)
            del int_list[0]
            del int_list[-1]
        if len(int_list) % 3 == 0 and len(int_list) > 1:
            uus1 = get_max_element(int_list)
            uus2 = get_min_element(int_list)
            print(int_list)
            uus3 = int(uus1) + int(uus2)
            new_int_list.append(uus3)
            del int_list[0]
            del int_list[-1]

    return sorted(new_int_list, reverse=True)
    pass


if __name__ == '__main__':
    #print(add_list_elements([0, 0, 0, 0, 0, 0, 1, 2, 5, 6]))  # -> [6, 5, 2, 1, 0]
    #print(add_list_elements([0, 0, 2, 0, 3, 4, 1, 2, 5, 6]))
    print(add_list_elements([-1, -2, -5, -50, -14]))  # -> [-16, -51]
    #print(add_list_elements([1]))  # -> []
