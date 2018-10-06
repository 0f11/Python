"""
janguru.py.

Olen kulutanu sellele juba 3 nädalat,, vaadates sellele ajale tagasi, ei kahetse ma miskit.
"""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """
    Lugu kahe jänese kohtumisest.

    :param pos1:
    :param jump_distance1:
    :param sleep1:
    :param pos2:
    :param jump_distance2:
    :param sleep2:
    :return:
    """
    current_time = 0
    p1 = pos1
    p2 = pos2
    k1 = jump_distance1 / sleep1
    k2 = jump_distance2 / sleep2
    if (jump_distance1 <= jump_distance2 and sleep1 == sleep2) or (pos1 < pos2 and k1 < k2) or (
            pos1 > pos2 and k1 > k2):
        return -1
    if p2 - p1 <= 0 and jump_distance2 - jump_distance1 <= 0:
        return -1
    if p1 == p2:
        return p1
    while p1 != p2:
        current_time = current_time + 1
        if current_time % sleep1 == 0:
            p1 = p1 + jump_distance1
        if current_time % sleep2 == 0:
            p2 = p2 + jump_distance2
        if p1 == p2:
            return p1


if __name__ == "__main__":
    print(meet_me(1, 2, 2, 1, 4, 4))
    print(meet_me(1, 2, 3, 4, 5, 5))
    print(meet_me(10, 7, 7, 5, 8, 6))
    print(meet_me(100, 7, 4, 300, 8, 6))
    print(meet_me(1, 7, 1, 15, 5, 1))
    print(meet_me(0, 1, 1, 1, 1, 1))
