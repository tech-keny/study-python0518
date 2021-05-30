value = list(map(int, input().split()))


li = []

for i in range(1,value[0]+1):
    li.append(i)



if value[1]*value[2] in li:
    if value[2] == 1:
        x = li[0:value[1]]
        x = list(map(str, x))
        print(' '.join(x))
    else:
        x = li[value[1]*(value[2]-1):value[1]*value[2]]
        x = list(map(str, x))
        print(' '.join(x))

elif value[1]*(value[2]-1)+1 in li:
    x = li[value[1]*(value[2]-1):]
    x = list(map(str,x))
    print(' '.join(x))
    
else:
    print('none')	