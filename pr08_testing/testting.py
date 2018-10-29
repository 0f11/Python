"""Testing.py."""

from shortest_way_back import shortest_way_back
import random

def test_north():
    assert shortest_way_back("N") == "S"


def test_south():
    assert shortest_way_back("S") == "N"


def test_west():
    assert shortest_way_back("W") == "E"


def test_east():
    assert shortest_way_back("EE") == "WW"


def test_empty_string():
    assert shortest_way_back("") == ""


def test_finish_home():
    assert shortest_way_back("WENS") == ""




