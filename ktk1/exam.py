import re

"""KTK1."""


def remove_middle_character(string: str):
    """
    Return a string where middle character is removed if the string length is equal to odd number.

    If the input string length is equal to even number return input string. In the case of empty string, return empty string.
    remove_middle_character("kalev") => "kaev"
    remove_middle_character("linda") => "linda"
    remove_middle_character("olevipoeg") => "olevpoeg"
    remove_middle_character("") => ""
    """
    answer = []
    if len(string) % 2 != 0:
        answer = string.split()
    print(answer)


def multiplication(number: int) -> list:
    """
    Return list, where input number is multiplicated with numbers from 1 to 10.

    There is no restriction to input numbers if only its type.

    multiplication(5) => [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    multiplication(0) => [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    answer_list = []
    for number_list in range(11):
        if number_list != 0:
            outcome = number_list * number
            answer_list.append(outcome)
    return answer_list


def chars_combinations(string: str) -> list:
    """
    Return all combinations of string characters by 2 string length is bigger than 1.

    Characters in results should follow their natural order in the input string.

    chars_combinations("habe") => ["ha", "hb", "he", "ab", "ae", "be"]
    chars_combinations("az") => ["az"]
    chars_combinations("s") => []
    chars_combinations("") => []
    """
    return re.findall(r'\w{2}', string)


print(chars_combinations("habe"))  # => ["ha", "hb", "he", "ab", "ae", "be"]
print(chars_combinations("az"))  # => ["az"]
print(chars_combinations("s"))  # => []
print(chars_combinations(""))  # => []
# print(remove_middle_character("kalev")) # => "kaev"
# print(remove_middle_character("linda"))  # => "linda"
# print(remove_middle_character("olevipoeg"))  # => "olevpoeg"
# print(remove_middle_character(""))  # => ""
