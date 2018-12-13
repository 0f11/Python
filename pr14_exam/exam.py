"""Exam.py."""


def segment_number(first_number, last_number):
    """
    Return list with elements dividable by 5 but not dividable by 3 between (inclusive) two arguments.

    Return list of numbers where only numbers between first_number
    and last_number (both inclusive) which divide by 5 but do not divide by 3
    are used.

    #1

    :param first_number: the lowest possible candidate
    :param last_number: the highest possible candidate
    :return: list of numbers
    """
    answer = []
    for i in range(first_number, last_number + 1):

        if i % 5 == 0 and i % 3 != 0:
            answer.append(i)

    return answer


def add_or_subtract(numbers, op=1):
    """
    Return the sum of all numbers in a list.

    The sum is calculated according to following rules:
        -always start by adding all the numbers together.
        -if you find a 0, start subtracting all following numbers until you find another 0, then start adding again.
        -there might be more than two 0 in a list - change +/- with every 0 you find.

    For example:
        [1, 2, 0, 3, 0, 4] -> 1 + 2 - 3 + 4 = 4
        [0, 2, 1, 0, 1, 0, 2] -> -2 - 1 + 1 - 2 = -4
        [1, 2] -> 1 + 2 = 3
        [4, 0, 2, 3] = 4 - 2 - 3 = -1

    #2
    print(add_or_subtract([1, 2, 0, 3]))# == 0
    print(add_or_subtract([0, 1, 2]))# == -3
    print(add_or_subtract([1, 2, 0, 2, 0, 4]))# == 5

    :param numbers: the list of number given.
    :return: the sum of all numbers.
    """
    if numbers.count(0) == 0:
        return sum(numbers) * op
    return sum(numbers[:numbers.index(0)]) * op + add_or_subtract(numbers[numbers.index(0) + 1:], op * -1)


def should_get_up_early(is_weekday, really_tired, first_class_is_programming):
    """
    Decide if you should get up early.

    You should only even consider getting up early if it is a weekday, on weekends you should never get up early.
    If it is a weekday you should typically get up early, unless you are really tired.
    But if it is a weekday and you are really tired but the first class is a programming class you should still get up
    early ignoring you being tired.

    #3

    :param is_weekday: is it a weekday or not, boolean
    :param really_tired: are you really tired, boolean
    :param first_class_is_programming: is the first class a programming class, boolean
    :return: True if you should get up early, otherwise False
    """
    if is_weekday == True or False and first_class_is_programming == True:
        return True
    if is_weekday == True and really_tired == False:
        return True
    else:
        return False


def pear_fear(pears, people):
    """
    Return how many pears non-pear-fearers get.

    Every 3rd person fears pears, so they won't get any.
    How many pears will each get?
    Everyone who is not afraid of pears gets equal number of pears.
    Only whole pears will be used, so some pears may remain.

    #4
    print(pear_fear(10, 3))  # == 5
    print(pear_fear(10, 5))  # == 2
    print(pear_fear(0, 3))  # == 0
    print(pear_fear(17, 2))  # == 8
    print(pear_fear(21, 10))  # == 3

    :param pears:
    :param people:
    :return:
    """
    if people == 3:
        return pears // 2
    no_fear_people = people // 3
    return pears // (people - no_fear_people)


def string_between_string(word1, word2):
    """
    Insert reversed word2 to the center of word1.

    word1 length is always even.

    #5

    :param word1: Initial word. String.
    :param word2: Word to reverse and insert. String.
    :return: New word as string.
    """
    index = int(len(word1) / 2)
    return word1[:index] + word2[::-1] + word1[index:]


def get_padded_string(string1, string2):
    """
    Pad the longer of two strings with the shorter one on both sides.

    If both strings are the same length, consider string1 as the longer one.
    For example when string1 is "pizza" and string2 is "bbq", this should return "bbqpizzabbq".

    #6
     print(get_padded_string("pizza", "bbq"))  # == "bbqpizzabbq"
    print(get_padded_string("dog", "cat"))  # == "catdogcat"
    print(get_padded_string("geoff", "giraffe"))  # == "geoffgiraffegeoff"

    :param string1: String one
    :param string2:  String two
    :return: Padded string
    """
    if len(string1) >= len(string2):
        return f"{string2}{string1}{string2}"
    else:
        return f"{string1}{string2}{string1}"


def remove_duplicate(number_list):
    """
    Return list where consecutive duplicates are removed.

    Go though given list and remove all
    occurrences of two or more of the same
    numbers appearing after one another.
    Remove all but one of the duplicates.
    assert remove_duplicate([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
    assert remove_duplicate([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicate([1, 1, 1, 1, 1, 2, 1, 1, 3]) == [1, 2, 1, 3]
    #7

    :param number_list: input list
    :return: new list
    """
    i = 0
    while i < len(number_list) - 1:
        if number_list[i] == number_list[i + 1]:
            del number_list[i]
        else:
            i = i + 1
    return number_list


def who_called(calls, name):
    """
    You are given a dictionary of calls and a name.

    Determine who called that name.
    If nobody called the person, return -1.

    #8

    :param calls: dictionary of all the calls
    :param name: name of the receiver
    :return: name of the caller
    """
    calls = dict(calls)
    if len(calls) == 0:
        return -1
    if name in calls.values():
        return calls[name]
    else:
        return -1


def remove_lowest_digit(number):
    """
    Given a non-negative integer, remove the first occurrence of the lowest digit and return a new number.

    123 => 23
    223 => 23
    232 => 32
    1 => 0
    :param number: non-negative integer
    :return: non-negative integer
       assert remove_lowest_digit(123) == 23
    assert remove_lowest_digit(100) == 10
    assert remove_lowest_digit(7) == 0
    assert remove_lowest_digit(171) == 71
    """
    numbers_list = []
    numbers = str(number)
    for i in numbers:
        numbers_list.append(i)
    if len(numbers_list) == 1:
        return 0
    numbers_list_2 = sorted(numbers_list)
    numbers_list.remove(numbers_list_2[0])
    return int("".join(numbers_list))


def show_highest_grade(grade1, grade2):
    """
    Print "Highest grade: GRADE" where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"

    #10

    :param grade1:
    :param grade2:
    :return:
    """
    if grade1 > grade2:
        print(f"Highest grade: {grade1}")
    else:
        print(f"Highest grade: {grade2}")
    return None
