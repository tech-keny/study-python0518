t = input().split()
t = list(map(int, t))   # int変換

temp = []
for i in range(t[0]):
    a = input().split()
    a = list(map(int, a))   # int変換
    temp.append(a)

h = [x[1] for x in temp]

temp_m = 101
d = [0, 1]

for i in range(t[1]-1, t[0]):
    j = i + 1

    m = sum(h[(j-t[1]):j]) / t[1]

    if m < temp_m:
        temp_m = m
        d = [j-t[1], i]

print(str(temp[d[0]][0]) + " " + str(temp[d[1]][0]))