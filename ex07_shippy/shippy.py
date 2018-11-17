"""Simulation."""

from typing import Tuple


def new_position(step, ship_pos):
    """
    Find new position.

    :param step: char
    :param ship_pos: list
    :return: list
    """
    d = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1)
    }
    position = ship_pos[:]

    if step == "N" or step == "S":
        position[0] += d[step][0]

    elif step == "E" or step == "W":
        position[1] += d[step][1]

    return position


def simulate(world_map: list, flight_plan: list) -> list:
    """
    Simulate a flying space ship fighting space pirates.

    :param world_map: A list of strings indicating rows that make up the space map.
                 The space map is always rectangular and the minimum given size is 1x1.
                 Space pirate free zone is indicated by the symbol ('-'), low presence by ('w') and high presence by ('W').
                 The ship position is indicated by the symbol ('X'). There is always one ship on the space map.
                 Asteroid fields are indicated by the symbol ('#').

    :param flight_plan: A list of moves.
                  The moves are abbreviated N - north, E - east, S - south, W - west.
                  Ignore moves that would put the ship out of bounds or crash it into an asteroid field.

    :return: A list of strings indicating rows that make up the space map. Same format as the given wmap.

    Pirates under Shippy's starting position are always eliminated ('-').
    If Shippy fights pirates in high presence area, it first turns into low presence ('w')
     and then from low presence into no presence area ('-').
    """
    list1 = list_to_dictionary_converter(world_map)

    world_map1 = list1[0]
    ship_pos = [list1[1], list1[2]]

    width = len(world_map[0])
    height = len(world_map)

    for step in flight_plan:
        new_position1 = new_position(step, ship_pos)

        if height > new_position1[0] >= 0 and width > new_position1[1] >= 0 \
                and world_map1[tuple(new_position1)] != "#":
            ship_pos = new_position1
            world_map1[tuple(ship_pos)] = change_character(world_map1[tuple(new_position1)])

    world_map1[tuple(ship_pos)] = "X"

    return dictionary_to_list_converter(world_map1, width, height)


def change_character(character):
    """
    Change character.

    :param character: character
    :return: character
    """
    if character == "W":
        character = "w"

    elif character == "w":
        character = "-"

    return character


def list_to_dictionary_converter(world_map: list) -> Tuple[dict, int, int]:
    """
    Convert a list to dictionary using coordinates as keys.

    :param world_map: list of strings.
    :return: dictionary of the space, shippy y position, shippy x position

    Map tile under Shippy's location is marked as "-" or no presence area.
    Dictionaries key is a Tuple which has Y-position as the first value and X-position as
    the second value. If there is no Shippy (Marked as X in the list) in the list, the
    coordinates are marked as 0 and 0.
    """
    d1 = {}
    x = 0
    y = 0
    for rowi, row in enumerate(world_map):

        for coli, col in enumerate(row):
            d1[rowi, coli] = col

            if col == 'X':
                x = rowi
                y = coli
                d1[x, y] = '-'
    return d1, x, y


def dictionary_to_list_converter(space_map: dict, width: int, height: int) -> list:
    """
    Convert dictionary of coordinates to list of strings.

    :param space_map: Dictionary of the space
    :param width: Width of the world.
    :param height: Height of the world.
    :return: List of strings

    PS: You should add Shippy back the the dictionary before you call this method.
    """
    list1 = []
    sortedlist = sorted(space_map.items())
    string = ""

    for key in sortedlist:

        if key[0][1] == 0:
            list1.append(string)
            string = ""
        list1[key[0][0]] += key[1]

    return list1


if __name__ == '__main__':
    space_list1 = [
        "#www-",
        "wXw#-",
    ]

    flight_plan1 = ["N", "E", "E", "S", "E"]
    print("\n".join(simulate(space_list1, flight_plan1)))
    print(list_to_dictionary_converter(flight_plan1))

    # #---X
    # w-w#-

    # assert simulate(space_list1, flight_plan1) == ["#---X", "w-w#-"]

    print()

    space_list2 = [
        "WWWW",
        "-wwW",
        "X-#W",
    ]

    flight_plan2 = ["N", "N", "E", "E", "S", "W", "W", "S", "E", "E"]
    print("\n".join(simulate(space_list2, flight_plan2)))

    # wwwW
    # ---W
    # -X#W

    # assert simulate(space_list2, flight_plan2) == ["wwwW", "---W", "-X#W"]

    # assert list_to_dictionary_converter(["-"]) == ({(0, 0): "-"}, 0, 0)
    # assert list_to_dictionary_converter(['W#', '-X']) == ({(0, 0): 'W', (0, 1): '#', (1, 0): '-', (1, 1): '-'}, 1, 1)
    #
    # assert list_to_dictionary_converter(
    #     world_map=space_list1
    # ) == ({(0, 0): '#', (0, 1): 'w', (0, 2): 'w', (0, 3): 'w', (0, 4): '-', (1, 0): 'w', (1, 1): '-', (1, 2): 'w',
    #        (1, 3): '#', (1, 4): '-'}, 1, 1)
    #
    # assert dictionary_to_list_converter(
    #     {(0, 0): '#', (0, 1): 'w', (0, 2): 'w', (0, 3): 'w', (0, 4): '-', (1, 0): 'w', (1, 1): 'X', (1, 2): 'w',
    #      (1, 3): '#', (1, 4): '-'}, 5, 2) == space_list1
    #
    # assert dictionary_to_list_converter({(0, 0): "X"}, 1, 1) == ["X"]
