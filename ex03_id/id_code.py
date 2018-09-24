"""Check if given ID code is valid."""


def check_your_id(id_code: str):
    """
    Check if given ID code is valid and return the result.

    :param id_code: str
    :return: boolean
    """
    str1 = id_code
    if len(str1) == int(11):
        return True
    else:
        return False
    pass


def check_gender_number(gender_number: int):
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if gender_number == range(1, 7):
        return True
    else:
        return False
    pass


def check_year_number_two_digits(year_number: int):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """

    if year_number < 10:
        str(year_number).lstrip("0")
    int(year_number)
    if year_number >= 100:
        return False
    if year_number < 100:
        return True
    else:
        return False
    pass


def check_month_number(month_number: int):
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if month_number < 10 and len(str(month_number)) == int(2):
        str(month_number).lstrip("0")
    int(month_number)
    if month_number <= 12:
        return True
    else:
        return False
    pass


def check_day_number(year_number: int, month_number: int, day_number: int):
    """
    Check if given value is correct for day number in ID code.
    Also, consider leap year and which month has 30 or 31 days.

    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    if month_number < 10 and len(str(month_number)) == int(2):
        str(month_number).lstrip("0")

    if year_number < 50:
        str(year_number).join(str(20) + str(year_number))
    elif year_number > 50:
        str(year_number).join(str(19) + str(year_number))
    int(year_number)
    int(month_number)
    int(day_number)
    if int(month_number) == 2 and day_number <= 29:
        return True
    elif int(month_number) % int(2) == 0 and int(month_number) <= 7 and int(day_number) <= 30:
        return True
    elif int(month_number) % 2 != 0 and int(month_number) > 7 and int(day_number) == 30:
        return True
    elif int(month_number) % 2 == 0 and int(month_number) > 7 and int(day_number) == 31:
        return True
    elif int(month_number) % 2 != 0 and int(month_number) <= 7 and int(day_number) == 31:
        return True
    else:
        return False
    pass


def check_leap_year(year_number: int):
    """
    Check if given year is a leap year.

    :param year_number: int
    :return: boolean
    """
    if int(year_number) % 400 == 0 or int(year_number) % 4 == 0:
        return True
    if int(year_number) % 100 == 0:
        return False
    pass


def check_born_order(born_order: int):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    int(born_order)
    return True
    pass


def check_control_number(id_code: str):
    """
    Check if given value is correct for control number in ID code.
    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    int(id_code)
    list_1 = [i for i in id_code]
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    kontroll = [int(list_1[i]) * int(x[i]) for i in range(len(x))]
    number = sum(kontroll) % 11
    if number == 0:
        y = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        kontroll2 = [int(list_1[i]) * int(y[i]) for i in range(len(y))]
        number = sum(kontroll2) % 11
        if number == 10:
            str(number).split("1")
    if number == list_1[-1]:
        return True
    else:
        return False
    pass


if __name__ == '__main__':
    print("Overall ID check::")
    print(check_your_id("49808270244"))  # -> True
    personal_id = input()  # type your own id in command prompt
    print(check_your_id(personal_id))  # -> True
    print(check_your_id("12345678901"))  # -> False
    print("\nGender number:")
    print("\nYear number:")
    print(check_year_number_two_digits(100))  # -> False
    print(check_year_number_two_digits(50))  # -> true
    print("\nMonth number:")
    print(check_month_number(2))  # -> True
    print(check_month_number(15))  # -> False
    print("\nDay number:")
    print(check_day_number(5, 12, 25))  # -> True
    print(check_day_number(10, 8, 32))  # -> False
    print(check_leap_year(1804))  # -> True
    print(check_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(check_day_number(96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(check_day_number(99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(check_day_number(8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(check_day_number(22, 4, 31))  # -> False (April contains max 30 days)
    print(check_day_number(18, 10, 31))  # -> True
    print(check_day_number(15, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(check_born_order(0))  # -> True
    print(check_born_order(850))  # -> True
    print("\nControl number:")
    print(check_control_number("49808270244"))  # -> True
    print(check_control_number("60109200187"))  # -> False, it must be 6
