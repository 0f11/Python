"""Recursion.py."""


def recursive_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using recursion.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    if not numbers:
        return 0
    counter = 0 if numbers[0] % 2 != 0 else numbers[0]
    return counter + recursive_sum(numbers[1:])


def loop_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using loops.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    answer = 0
    for x in numbers:
        if x % 2 == 0:
            answer = answer + x

    return answer
    pass


def loop_reverse(s: str) -> str:
    """Reverse a string using a loop.

    :param s: string
    :return: reverse of s
    """
    return s[::-1]


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    :param s: string
    :return: reverse of s
    """
    if s == "":
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]
    pass


if __name__ == '__main__':
    print(recursive_sum([1, 3, 5, 7, 9]))
    print(recursive_sum([2, 4, 5, 8]))
    print(loop_sum([1, 3, 5, 7, 9]))
    print(loop_sum([2, 4, 5, 8]))
    print(recursive_reverse("abcdef"))
    print(loop_reverse("abcdef"))
