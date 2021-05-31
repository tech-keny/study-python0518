num = int(input())

amount = 0
# set_number = 1

li = []
for i in range(num):
    x = int(input())
    li.append(x)
    
for j in range(num):
    if j ==0:
        amount += abs(li[j]-1)
    else:
        amount += abs(li[j-1] -li[j])

print(amount)