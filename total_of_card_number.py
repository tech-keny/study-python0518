num = int(input())

li = input().split()
count = 0
if 'x10' in li:
    li.remove('x10')
    li = list(map(int, li))
    if 0 in li:
        li.remove(max(li))
        for i in range(len(li)):
            count += li[i]
        print(count*10)
    else:
        for i in range(len(li)):
            count += li[i]
        print(count*10)
else:
    li = list(map(int,li))
    if 0 in li:
        li.remove(max(li))
        for i in range(len(li)):
            count += li[i]
        print(count)
    else:
        for i in range(len(li)):
            count += li[i]
        print(count)
        
        
            
        