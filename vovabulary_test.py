# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def judje():
    global count, result
    for j in range(len(max(x,key=len))):
        if len(x[0]) == len(x[1]):
            if x[0][j] != x[1][j]:
                count +=1
            
        else:
            break
            
            

a = int(input())

result = 0
for i in range(a):
    n = input()
    x = n.split()
    if x[0] == x[1]:
            result +=2
    else:
        count = 0
        judje()
        
        if count == 1:
            result +=1
            
        else:
            result +=0
        

print(result)
            
            
            
            
    