num = list(map(int, input().split()))

left = num[1]
machine = 0
li = []

for i in range(num[0]):
    x = int(input())
    li.append(x)
    m = num[1] % x
    if m < left:
        left = m
        machine = x
    elif m == left:
        if x > machine:
            left = m
            machine = x
            
print(li.index(machine)+1)
    