"""
janguru.py.

Olen kulutanu sellele juba 3 nädalat, vaadates sellele ajale tagasi, ei kahetse ma miskit.
"""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    pos_x1 = pos1 + jump_distance1
    pos_x2 = pos2 + jump_distance2
    aeg = sleep1
    aeg2 = sleep2
    if pos2 - pos1 and jump_distance2 - jump_distance1 == 0:
        return print("-1")
    if jump_distance1 <= jump_distance2 and pos1 <= pos2 and int(
            (jump_distance1 / sleep1) < int(jump_distance2 / sleep2)):
        return print("-1")
    while pos_x1 != pos_x2:
        aeg = aeg + 1
        aeg2 = aeg2 + 1
        if aeg % sleep1 == 0:
            pos_x1 = pos_x1 + jump_distance1
        elif pos_x1 == pos_x2:
            break
        if aeg2 % sleep2 == 0:
            pos_x2 = pos_x2 + jump_distance2
        elif pos_x1 == pos_x2:
            break
    print(f"{pos_x2}")
