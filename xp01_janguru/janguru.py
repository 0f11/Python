def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """ Jänkude algpositsioonid. """

    hype1 = (jump_distance1 / sleep1) * sleep1
    hype2 = (jump_distance2 / sleep2) * sleep2
    pos_x1 = pos1 + hype1
    pos_x2 = pos2 + hype2
    aeg = 1 / sleep1
    aeg2 = 1 / sleep2

    if pos2 - pos1 and jump_distance2 - jump_distance1 == 0:
        return print("-1")
    if jump_distance1 <= jump_distance2 and pos1 <= pos2 and ((pos2 - pos1) % (jump_distance2 - jump_distance1) == 0):
        return print("-1")
    while pos_x1 != pos_x2:
        aeg = aeg + (1 / sleep1)
        aeg2 = aeg2 + (1 / sleep2)
        aeg = aeg + sleep1
        aeg2 = aeg2 + sleep2

        if aeg >= sleep1:
            pos_x1 = pos_x1 + jump_distance1
        if aeg2 >= sleep2:
            pos_x2 = pos_x2 + jump_distance2
        if pos_x1 == pos_x2:
            break

    print(f"{pos_x2}")
    # print(f"{aeg}")
    # print(f"{aeg2}")
    # print(f"{counter}")


meet_me(1, 2, 1, 2, 1, 1)  # => 3
meet_me(1, 2, 3, 4, 5, 5)  # => -1
meet_me(10, 7, 7, 5, 8, 6)  # => 45
meet_me(100, 7, 4, 300, 8, 6)  # => 940
meet_me(1, 7, 1, 15, 5, 1)  # => 50
meet_me(0, 1, 1, 1, 1, 1)  # => -1
