"""Testing.py."""

from shortest_way_back import shortest_way_back
import random


def test_north():
    assert shortest_way_back("S") == "N"


def test_north_long():
    assert shortest_way_back("SSS") == "NNN"


def test_south():
    assert shortest_way_back("N") == "S"


def test_south_long():
    assert shortest_way_back("NNN") == "SSS"


def test_west():
    assert shortest_way_back("E") == "W"


def test_west_long():
    assert shortest_way_back("EEE") == "WWW"


def test_east():
    assert shortest_way_back("W") == "E"


def test_east_long():
    assert shortest_way_back("WWW") == "EEE"


def test_empty_string():
    assert shortest_way_back("") == ""


def test_finish_home():
    assert shortest_way_back("WENS") == ""


