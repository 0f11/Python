"""
janguru.py.

Täiesti random

"""

pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2 = map(int, input().split())

# Note: 0 <= x1 < x2 <= 10000
# x1 + k.v1 = x2 + k.v20,

if (jump_distance2 < jump_distance1) and ((pos2 - pos1) % (jump_distance2 - jump_distance1)) == 0:
    print("YES")
else:
    print("NO")
