num = int(input())

li = []

for i in range(num):
    x = input()
    li.append(x)

rl = [] 
 
for j in range(4):
    count = 0
    for k in range(num):
        count += li[k][j].count('1')
        
    if count % 2 ==0:
        rl.append('0')   
    elif count %2 !=0:
        rl.append('1')
        
print(''.join(rl))
         