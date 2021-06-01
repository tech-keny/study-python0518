num = list(map(int, input().split()))
li = input().split()

x = sorted(li)

result = x[num[1]*num[2]-num[1]:num[1]*num[2]]

second_result = x[num[1]*num[2]-num[1]:]

if num[1]*num[2] <= num[0]:
    for i in result:
        print(i)
else:
    for i in second_result:
        print(i)

