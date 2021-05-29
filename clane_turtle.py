data = input().split()
d = list(map(int, data))

matched = [0, 0]
for i in range(1, d[1]):
    tmp_feet = i * d[2] + (d[1] - i) * d[3]
    if tmp_feet == d[0]:
        if matched != [0, 0]:
            matched = [0, 0]
            break
        else:
            matched = [i, d[1] - i]
if matched != [0, 0]:
    print(matched[0], matched[1])
else:
    print('miss')
