# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())


r = []
s = []
for i in range(n):
    x = input()
    li = x.split()
    r.append(li)
    
for j in range(n):
    for k in range(4):
        s.append(int(r[j][k]))

result = []




result.append(r[0][0])
result.append(r[n-1][1])
result.append(max(s))
result.append(min(s))

result_correct = [result[0],result[1],str(result[2]),str(result[3])]
outcome = ' '.join(result_correct)
print(outcome)
