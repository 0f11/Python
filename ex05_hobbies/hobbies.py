"""hobbies.py."""
import csv
from collections import Counter
from itertools import takewhile


def create_list_from_file(file):
    """
    Collect lines from given file into list..

    :param file: original file path
    :return: list of lines
    """
    data = open(file, "r")

    list1 = data.readlines()

    data.close()

    return list1


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    list1 = create_list_from_file(file)
    hobbies = {}
    for element in list1:
        new_list = element.replace("\n", "").replace(":", " ").split()
        hobbies.setdefault(new_list[0], [])
        if new_list[1] not in hobbies[new_list[0]]:
            hobbies[new_list[0]].append(new_list[1])
    return hobbies


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    dict1 = create_dictionary(file)
    list1 = []
    person = ""
    most = 0

    for i in dict1:
        most = len(dict1[i])
        person = i
        break

    for x in dict1:
        if most < len(dict1[x]):
            most = len(dict1[x])
            person = x

    list1.append(person)

    for y in dict1:
        if len(dict1[y]) == most and y != person:
            list1.append(y)

    return list1


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    dict1 = create_dictionary(file)
    list1 = []
    person = ""
    least_hobbies = 0

    for i in dict1:
        least_hobbies = len(dict1[i])
        person = i
        break

    for x in dict1:
        if least_hobbies > len(dict1[x]):
            least_hobbies = len(dict1[x])
            person = x

    list1.append(person)

    for y in dict1:
        if len(dict1[y]) == least_hobbies and y != person:
            list1.append(y)

    return list1


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    dict1 = create_dictionary(file)
    c = Counter()
    for d in dict1.values():
        c += Counter(d)

    return [c.most_common(1)[0][0]]


def find_least_popular_hobby(file):
    """
    Find the least popular hobby..

    :param file: original file path
    :return: list
    """
    dict1 = create_dictionary(file)
    c = Counter()
    for d in dict1.values():
        c += Counter(d)
    popular = c.most_common(0)[0][1]
    return list(takewhile(lambda x: x[1] == popular, c.most_common()))


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])

        dict1 = create_dictionary(file)

        for k, v in dict1.items():
            string_hobbies = "-".join(element for element in v)
            writer.writerow([k, string_hobbies])


# These examples are based on a given text file from the exercise.


if __name__ == '__main__':
    dic = create_dictionary("hobbies_database.txt")
    # print(len(create_list_from_file("hobbies_database.txt")))  # -> 100
    # print("Check presence of hobbies for chosen person:")
    # print("shopping" in dic["Wendy"])  # -> True
    # print("fitness" in dic["Sophie"])  # -> False
    # print("gaming" in dic["Peter"])  # -> True
    # print("Check if hobbies - person relation is correct:")
    # print("Check if a person(people) with the biggest amount of hobbies is(are) correct:")
    # print(find_person_with_most_hobbies("hobbies_database.txt"))  # -> ['Jack']
    # print(len(dic["Jack"]))  # ->  12
    # print(len(dic["Carmen"]))  # -> 10
    # print("Check if a person(people) with the smallest amount of hobbies is(are) correct:")
    # print(find_person_with_least_hobbies("hobbies_database.txt"))  # -> ['Molly']
    # print(len(dic["Molly"]))  # -> 5
    # print(len(dic["Sophie"]))  # -> 7
    # print("Check if the most popular hobby(ies) is(are) correct")
    print(find_most_popular_hobby("hobbies_database.txt"))  # -> ['gaming', 'sport', 'football']
    # print("Check if the least popular hobby(ies) is(are) correct")
    # print(find_least_popular_hobby("hobbies_database.txt"))  # -> ['tennis', 'dance', 'puzzles', 'flowers']
    # write_corrected_database("hobbies_database.txt", 'correct_hobbies_database.csv')
