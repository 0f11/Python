"""Make life easier whilst volunteering in a, French language camp."""


def count_portions(number_of_participants: int, day: int) -> int:
    """
    Count the total of portions served to participants during the camp recursively.

    There are 4 meals in each day and we expect that every participant eats 1 portion
    per meal. At the end of each day one participant leaves the camp and is not ours to
    feed.

    We are only counting the participants' meals, the organisers and volunteers
    eat separately. In case of negative participants or days the number of meals is
    still 0.

    count_portions(0, 7) == 0
    count_portions(6, 0) == 0
    count_portions(-8, 5) == 0
    count_portions(9, -5) == 0

    count_portions(6, 1) == 24
    count_portions(6, 2) == 44
    count_portions(6, 3) == 60

    :param number_of_participants: the initial number of participants.
    :param day: the specified day.
    :return: a total of portions served during the camp at the end of the specified day.
    """
    if day <= 0 or number_of_participants <= 0:
        return 0
    food = number_of_participants * 4
    new_day = day - 1
    people = number_of_participants - 1
    if new_day == 0:
        return food + count_portions(people, new_day)
    else:
        test = food + count_portions(people, new_day)
    return test


def names_to_be_eliminated(points_dict: dict, names: set = None, lowest_score: int = None) -> set:
    """
    Recursively find the names that are to be eliminated.

    When two or more people have the same lowest score, return a list in which every lowest
    scoring person is listed.

    names_to_be_eliminated({}) == set()
    names_to_be_eliminated({"Dylan": 10}) == {"Dylan"}
    names_to_be_eliminated({"Carl": 4, "Bert": -10}) == {"Bert"}
    names_to_be_eliminated({"Terry": 4, "Pete": 4}) == {"Terry", "Pete"}

    :param points_dict: dictionary containing name strings as
                        keys and points integers as values.
    :param names: helper to store current names
    :param lowest_score: helper to store current lowest score
    :return: set of names of lowest scoring people.
    """
    if len(points_dict) == 0:
        return set()
    answer = min(points_dict, key=lambda x: points_dict[x])
    return {f"{answer}"}


def people_in_the_know(hours_passed, cache: dict = None) -> int:
    """
    Return the number of people who know a rumor given the hours passed from the initial release.

    Every hour there is a recess where everybody can talk to everybody. Rumors always spread in
    the same fashion: everybody who are in the know are silent one recess after the recess they
    were told of the rumor. After that they begin to pass it on, one person per recess.

    people_in_the_know(0) == 0
    people_in_the_know(1) == 1
    people_in_the_know(2) == 1
    people_in_the_know(3) == 2
    people_in_the_know(4) == 3
    people_in_the_know(7) == 13

    :param hours_passed: the hours passed from the initial release.
    :param cache: helper to store already calculated results..
    :return: the number of people that have heard the rumor.
    """
    if hours_passed < 2:
        return hours_passed
    return people_in_the_know(hours_passed - 2) + people_in_the_know(hours_passed - 1)


def traversable_coordinates(world_map: list, coord: tuple = (0, 0), traversable_coords: set = None) -> set:
    """
    Return the coordinates that are traversable by humans or adjacent to, traversable coordinates.

    Given a two-dimensional list as a map, give the coordinates of traversable cells with the
    coordinates of cells which are adjacent to traversable cells with respect to the
    beginning coordinate.

    If there is not a traversable path from the beginning coordinate
    to the traversable cell, the traversable cell coordinate is not returned. Traversable
    cells are represented by empty strings. If the beginning coordinate cell is not traversable,
    return empty set.

    Coordinates are in the format (row, column). Negative coordinate values are considered invalid.
    world_map is not necessarily rectangular. Paths can be made through a diagonal.

    traversable_coordinates([]) == set()
    traversable_coordinates([[]]) == set()
    traversable_coordinates([["", "", ""]], (5, 2)) == set()
    traversable_coordinates([["1", "1", ""]], (-4, -9)) == set()
    traversable_coordinates([["1", [], "1"]], (0, 1)) == set()

    world = [["1", "1", "1", "1", "1"],
             ["1", "1", "1",  "", "1"],
             ["1", "1",  "", "1", "1"],
             ["1", "1",  "", "1", "1"],
             ["1", "1", "1", "1", "1"]]

    traversable = {(0, 2), (0, 3), (0, 4),
                   (1, 1), (1, 2), (1, 3), (1, 4),
                   (2, 1), (2, 2), (2, 3), (2, 4),
                   (3, 1), (3, 2), (3, 3),
                   (4, 1), (4, 2), (4, 3)}

    traversable_coordinates(world, (2, 2)) == traversable

    :param world_map: two-dimensional list of strings.
    :param coord: the (beginning) coordinate.
    :param traversable_coords:: helper to store traversable coordinates.
    :return: set of traversable and traversable-adjacent cell
            coordinate tuples with respect to starting coord
    """
    if traversable_coords is None:
        traversable_coords = set()

    if len(world_map) == 0 or len(world_map[0]) == 0 or len(coord) == 0:
        return traversable_coords

    if coord[1] > len(world_map[0]) or coord[1] < 0 or coord[0] > len(world_map) or coord[0] < 0:
        return traversable_coords

    if coord in traversable_coords:
        return traversable_coords

    else:
        traversable_coords.add(coord)

    if world_map[coord[0]][coord[1]] == "":
        for y in range(coord[0] - 1, coord[0] + 2):
            for x in range(coord[1] - 1, coord[1] + 2):
                traversable_coordinates(world_map, (y, x), traversable_coords)

    return traversable_coords
