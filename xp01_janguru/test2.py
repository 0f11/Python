pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2 = map(int, input().split())
pos_x1 = pos1 + ((jump_distance1 / sleep1) * sleep1)
pos_x2 = pos2 + ((jump_distance2 / sleep2) * sleep2)
pos_x1 = pos_x1 + jump_distance1
pos_x2 = pos_x2 + jump_distance2
print(f"{pos_x1}{pos_x2}")