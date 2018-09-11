"""
janguru.py.

Täiesti random
"""
pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2 = map(int, input().split())
pos_x1 = pos1 + ((jump_distance1 / sleep1) * sleep1)
pos_x2 = pos2 + ((jump_distance2 / sleep2) * sleep2)
meeting = pos_x1 == pos_x1

counter = 1

while meeting == False:
    counter =+ 1
    int((pos_x1 + jump_distance1)) and int((pos_x2 + jump_distance2))

    print(f"{counter}")
if meeting == True:
    counter =+ 1
    print(f"{counter}")
else:
    print("-1")
