"""
janguru.py.

Täiesti random
"""



def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """ Jänkude algpositsioonid."""
    hype1 = (jump_distance1 / sleep1) * sleep1
    hype2 = (jump_distance2 / sleep2) * sleep2
    pos_x1 = pos1 + hype1
    pos_x2 = pos2 + hype2

    if pos2 - pos1 and jump_distance2 - jump_distance1 == 0:
        print("-1")
        return
    elif jump_distance1 <= jump_distance2 and pos1 <= pos2 and ((pos2 - pos1) % (jump_distance2 - jump_distance1) == 0):
        print("-1")
        return
    counter = 1
    if counter >= 1000:
        exit()
    while pos_x1 != pos_x2:

        counter = counter + 1
        pos_x1 = pos_x1 + hype1
        pos_x2 = pos_x2 + hype2
    print(f"{pos_x1}")
    print(f"{counter}")


# pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2 = map(int, input().split())
meet_me(2, 1, 1, 1, 2, 1)
# meet_me(1, 2, 3, 4, 5, 5)
meet_me(10, 7, 7, 5, 8, 6)
# meet_me(100, 7, 4, 300, 8, 6)
#meet_me(1, 7, 1, 15, 5, 1)
#meet_me(0, 1, 1, 1, 1, 1)
"""
meet_me(1, 2, 1, 2, 1, 1) => 3
meet_me(1, 2, 3, 4, 5, 5) => -1
meet_me(10, 7, 7, 5, 8, 6) => 45
meet_me(100, 7, 4, 300, 8, 6) => 940
meet_me(1, 7, 1, 15, 5, 1) => 50
meet_me(0, 1, 1, 1, 1, 1) => -1
"""

# hype1 = (jump_distance1 / sleep1) * sleep1
# hype2 = (jump_distance2 / sleep2) * sleep2
# pos_x1 = pos1 + hype1
# pos_x2 = pos2 + hype2.
# if pos2 - pos1 and jump_distance2 - jump_distance1 == 0:
#    print("-1")
#    exit("Ei kohtu")
# if pos1 <= pos2 and jump_distance1 <= jump_distance2 and ((pos2 - pos1) % (jump_distance2 - jump_distance1) == 0):
#    print("-1")
#    exit("Ei kohtu")
# while pos_x1 != pos_x2:
#    pos_x1 = pos_x1 + jump_distance1
#    pos_x2 = pos_x2 + jump_distance2
#
# print(f"{pos_x1}")
