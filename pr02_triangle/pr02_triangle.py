"""Triangle info."""

import math


def find_triangle_info(a, b, c):

    """
    Write a function which finds perimeter, area and type of triangle based on given side lengths. (Note: a <= b <= c).

    The function should print "{type_by_length} {type_by_angle} triangle with perimeter of {perimeter} units and
    area of {area} units".
    IE: sides 3, 4, 5 should print "Scalene right triangle with perimeter of 12.0 units and area of 6.0 units".
    :return: None
    """
    perimeter = a + b + c
    pindala1 = (a + b + c) / 2
    area = round(math.sqrt(pindala1 * (pindala1 - a) * (pindala1 - b) * (pindala1 - c)), 2)

    if a == b == c:
        type_by_length = "Equilateral"
    elif a == b or b == c or a == c:
        type_by_length = "Isosceles"
    elif a != b != c:
        type_by_length = "Scalene"

    if (a * a) + (b * b) == (c * c):
        type_by_angle = "right"
    elif (a * a) + (b * b) < (c * c):
        type_by_angle = "obtuse"
    elif (a * a) + (b * b) > (c * c):
        type_by_angle = "acute"

    print(f"{type_by_length} {type_by_angle} triangle with perimeter of {perimeter} units and area of {area} units")


# if __name__ == "__main__":  # <- This line is needed for automatic testing

find_triangle_info(4, 5, 6)  # Scalene acute triangle with perimeter of 15.0 units and area of 9.92 units
find_triangle_info(4, 4, 6)  # Isosceles obtuse triangle with perimeter of 14.0 units and area of 7.94 units
