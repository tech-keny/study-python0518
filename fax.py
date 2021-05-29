m = int(input())
paper = int(input())

count = 0
mid_num = 0
result = 0

li = []



for i in range(paper):
    x = input().split()
    x = list(map(int, x))
    li.append(x)
    time = li[0][0]
    
for j in range(paper):  
    if time == li[j][0]:
        if li[j][1] <= 59:
            count += li[j][2]
    else:
        if count % m ==0:
            mid_num = count//m
        else:
            mid_num = count//m +1 
            
        result += mid_num
        count = 0
        if li[j][1] <= 59:
            count += li[j][2]
        mid_num = 0
        time = li[j][0]
        
if count % m == 0:
    mid_num += count//m
else:
    mid_num += count//m +1

result += mid_num

print(result)


    
    
    