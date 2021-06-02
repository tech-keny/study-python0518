import math

num = list(map(int, input().split()))

kcal = []

for i in range(num[0]):
    x = int(input())
    kcal.append(x)

stu = []  
count = 0
for j in range(num[1]):
    y = list(map(int,input().split()))
    for k in range(num[0]):
        val = (y[k] / 100)*kcal[k]
        count += math.floor(val)
    
    stu.append(count)
    count = 0
    
for l in range(len(stu)):
    print(stu[l])

