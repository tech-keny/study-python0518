value = list(map(int, input().split()))

li = []

for i in range(value[0]):
    x = list(map(int,input().split()))
    li.append(x)

time = 0
length = 0
flag = True 
# if li[0][1] == 0:
#     for k in range(1,value[0]):
#         if (li[k][1]-length) / (li[k][0] - time) <= value[1]:
#             flag = True
#             length = li[k][1]
#             time = li[k][0]
#         else:
#             flag = False
#             break
# else:
for j in range(value[0]):
    if li[j][0] - time == 0:
        continue
    
    elif (li[j][1]-length) / (li[j][0] - time) <= value[1]:
        flag = True
        length = li[j][1]
        time = li[j][0]
    else:
        flag = False
        break
        
if flag == True:
    print('NO')
else:
    print('YES')