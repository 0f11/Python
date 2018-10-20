""" Esimene tunnikontroll."""


def sum_odds_or_evens(a, b):
    """
    Given two numbers, return the sum of these numbers if they both are even or odd numbers, otherwise return None.

    Consider that zero is also even number.

    sum_odds_or_evens(2, 19) → 12
    sum_odds_or_evens(17, 31) → 48
    sum_odds_or_evens(99, 100) → None

    :param a: an integer.
    :param b: an integer.
    :return: The sum of a and b if they are even or odd numbers, otherwise None.
    """
    if a % 2 == 0 and b % 2 == 0 or a % 2 != 0 and b % 2 != 0:
        return int(a) + int(b)
    else:
        return None


if __name__ == '__main__':
    print(sum_odds_or_evens(99, 100))
    # print(first_and_last_item([5, 2, 7]))
    # print(exchange_first_and_last('vaal'))
    # print(remove_nth_symbol(sadam, 3))
    # print(repeated_word_numeration(["Uhti", "uhti", "uhkesti"]))
