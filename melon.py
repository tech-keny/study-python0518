num = int(input())

li = []

for j in range(num):
    x = input()
    li.append(x)
    
n = [i for i,x in enumerate(li) if x =='melon']
if 'melon' in li:
    s = n[0]

count = 1
for k in range(len(n)):
    if n[k]-s > 10:
        count += 1
        s = n[k]
if 'melon' in li:        
    print(count)
    
else:
    print(0)
    
    
