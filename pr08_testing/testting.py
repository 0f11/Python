"""Testing.py."""

import pytest
import shortest_way_back
import random


def test_shortest_way_back():
    """
    Test.

    :return:
    """
    assert "SSS" in shortest_way_back("NNN")
    assert "NN" in shortest_way_back("SS")
    assert "W" in shortest_way_back("E")
    assert "EEEE" in shortest_way_back("WWWW")
    assert "" in shortest_way_back("")
    assert "" in shortest_way_back("NESW")
    assert shortest_way_back("NNEESEW") in ["SWW", "WSW", "WWS"]

def test_random():
    assert random in shortest_way_back(random)
