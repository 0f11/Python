"""Testing.py."""

from shortest_way_back import shortest_way_back
import random


def shortest_way_back_correct(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    d = {
        "N": (1, 0),
        "S": (-1, 0),
        "E": (0, 1),
        "W": (0, -1)}

    lat = 0
    long = 0

    for direction in path:
        if direction == "N":
            lat = lat + d["N"][0]

        elif direction == "S":
            lat = lat + d["S"][0]

        elif direction == "E":
            long = long + d["E"][1]

        elif direction == "W":
            long = long + d["W"][1]

    return midaiganes(lat, long)


def midaiganes(lat, long):
    """
    Liiga palju ife.

    :param lat:
    :param long:
    :return:
    """
    tagasitee = []
    while True:
        if lat > 0:
            lat = lat - 1
            tagasitee.append("S")
        elif lat < 0:
            lat = lat + 1
            tagasitee.append("N")
        if long > 0:
            long = long - 1
            tagasitee.append("W")
        elif long < 0:
            long = long + 1
            tagasitee.append("E")
        if lat == 0 and long == 0:
            break
    return "".join(tagasitee)


def test_north():
    """
    Test north.

    :return:
    """
    assert shortest_way_back("S") == "N"


def test_north_long():
    """
    Test north long.

    :return:
    """
    assert shortest_way_back("SSS") == "NNN"


def test_south():
    """
    Test south.

    :return:
    """
    assert shortest_way_back("N") == "S"


def test_south_long():
    """
    Test south long.

    :return:
    """
    assert shortest_way_back("NNN") == "SSS"


def test_west():
    """
    Test west.

    :return:
    """
    assert shortest_way_back("E") == "W"


def test_west_long():
    """
    test west long.

    :return:
    """
    assert shortest_way_back("EEE") == "WWW"


def test_east():
    """
    Test east.

    :return:
    """
    assert shortest_way_back("W") == "E"


def test_east_long():
    """
    Test east long.

    :return:
    """
    assert shortest_way_back("WWW") == "EEE"


def test_empty_string():
    """
    Test empty.

    :return:
    """
    assert shortest_way_back("") == ""


def test_finish_home():
    """
    Test finish home.

    :return:
    """
    assert shortest_way_back("WENS") == ""


def test_only_valid():
    """
    Test random.

    :return:
    """
    for i in range(100):
        path = random.choices("NSWE", k=50)
        result = sorted(shortest_way_back(path))
        answer = sorted(shortest_way_back_correct(path))
        assert result == answer
