import random

v = input().split()


li = []

for i in range(12):
    random.shuffle(v)
    li.append(int(v[0]+v[1]) + int(v[2]+v[3]))

    
    
print(max(li))