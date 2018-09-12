"""
janguru.py.

Täiesti random
"""
pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2 = map(int, input().split())
pos_x1 = pos1 + ((jump_distance1 / sleep1) * sleep1)
pos_x2 = pos2 + ((jump_distance2 / sleep2) * sleep2)
if pos1 <= pos2 and jump_distance1 <= jump_distance2 and ((pos2 - pos1) % (jump_distance2 - jump_distance1) == 0):
    print("-1")
while pos_x1 != pos_x2:
    pos_x1 = pos_x1 + jump_distance1
    pos_x2 = pos_x2 + jump_distance2

print(f"{pos_x1}")
"""
meet_me(1, 2, 1, 2, 1, 1) => 3
meet_me(1, 2, 3, 4, 5, 5) => -1
meet_me(10, 7, 7, 5, 8, 6) => 45
meet_me(100, 7, 4, 300, 8, 6) => 940
meet_me(1, 7, 1, 15, 5, 1) => 50
meet_me(0, 1, 1, 1, 1, 1) => -1
"""
