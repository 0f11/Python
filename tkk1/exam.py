"""Esimene tunnikontroll."""


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


def first_and_last_item(num_list):
    """
    Given an list of number of ints, return a new list with length 2 containing the first and last.

    The initial list will be length 1 or more.

    first_and_last_item([9, 1, 5, 2, 7]) → [9, 7]
    first_and_last_item([1, 2, 3, 4]) → [1, 4]
    first_and_last_item([91, 4, 6, 52]) → [91, 52]

    :param nums: List of integers.
    :return: List with the first and the last element from the input list.
    """
    return [num_list[0], num_list[-1]]


def exchange_first_and_last(word):
    """
    Given a word as a string, return a string where first and last character are exchanged if last character is smaller.

    then first one, otherwise return intital word.

    Also, if the length of input word is smaller than one return empty string.

    exchange_first_and_last('kala') → 'aalk'
    exchange_first_and_last('kalalaev') → 'kalalaev'
    exchange_first_and_last('r') → 'r'
    exchange_first_and_last('') → ''

    :param word: input string.
    :return: a string
    """
    word1 = []
    word2 = []
    for i in word:
        word1.append(i)
        word2.append(i)

    if word == "":
        return ""

    elif word1[0] > word1[-1]:
        del word1[0]
        del word1[-1]
        word1.append(word2[0])
        word1.insert(0, word2[-1])
        return "".join(word1)
    else:
        return word


def remove_nth_symbol(s, n):
    """
    Return a new string where n-th symbol is removed.

    If the n is outside of the string, return original string.
    If n is 1, the first symbol is removed etc.

    remove_nth_symbol("tere", 1) => "ere"
    remove_nth_symbol("tere", 3) => "tee"
    remove_nth_symbol("tere", 5) => "tere"

    :param s: Input string.
    :param n: Which element to remove.
    :return: String where n-th symbol is removed.
    """
    output = []
    for i in s:
        output.append(i)

    if n <= len(s):
        del output[n - 1]
        return "".join(output)
    else:
        return s


def repeated_word_numeration(words_list):
    """
    For a given list of words, add numeration for every repeated word.

    The input list consists of words. For every repeated element in the input list,
    the output list adds a numeration after the words.
    The format is as follows: #N, where N starts from 1.
    Word comparison should be case-insensitive.
    The case of symbols in a word itself in output list should remain the same as in input list.

    The output list has the same amount of elements as the input list.
    For every repeated element in the output list, "#N" is added, where N = 1, 2, 3, ...

    word_numeration(["tere", "tere", "tulemast"]) => ["tere#1", "tere#2", "tulemast"]
    word_numeration(["Tere", "tere", "tulemast"]) => ["Tere#1", "tere#2", "tulemast"]
    word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]) => ["Tere#1", "tere#2", "tulemast#1"

    :param words: A list of strings.
    :return: List of words where repeated words have numeration.
    """
    vastus = []
    n = 0
    for i in words_list:
        if vastus:
            n = n + 1
            vastus.append(i + "#" + str(n))
        else:
            vastus.append(i)
            # print(vastus)
    return "".join(vastus)


if __name__ == '__main__':
    print(repeated_word_numeration(["tere", "tere", "tulemast"]))  # = > ["tere#1", "tere#2", "tulemast"]
    print(repeated_word_numeration(["Tere", "tere", "tulemast"]))  # = > ["Tere#1", "tere#2", "tulemast"]
    print(repeated_word_numeration(["Tere", "tere", "tulemast", "no", "tere",
                                    "TERE"]))  # = > ["Tere#1", "tere#2", "tulemast#1", "no","tere#3", "TERE#4"]
