"""Triangle info."""

import math


def find_triangle_info(a, b, c):
    """
    Write a function which finds perimeter, area and type(eg: isosceles right triangle) of triangle based on given side
    lengths. (Note: a <= b <= c).

    The function should print "{type_by_length} {type_by_angle} triangle with perimeter of {perimeter} units and
    area of {area} units".
    IE: sides 3, 4, 5 should print "Scalene right triangle with perimeter of 12.0 units and area of 6.0 units".
    :return: None
    """

    ymbermoot = float(a + b + c / 2)
    pindala = float(math.sqrt(ymbermoot * (ymbermoot - a)(ymbermoot - b)(ymbermoot - c)))

    if __name__ == "__main__":  # <- This line is needed for automatic testing
        find_triangle_info(4, 5, 6)  # Scalene acute triangle with perimeter of 15.0 units and area of 9.92 units
        find_triangle_info(4, 4, 6)  # Isosceles obtuse triangle with perimeter of 14.0 units and area of 7.94 units
