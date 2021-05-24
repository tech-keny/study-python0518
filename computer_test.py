# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def judge():
    global x, y
    if li[0] == 'SET' and li[1] == '1' :
        x = int(li[2])
    elif li[0] == 'SET' and li[1] == '2' :
        y = int(li[2])
    elif li[0] == 'ADD':
        y = x + int(li[1])
    elif li[0] == 'SUB':
        y = x- int(li[1])

x = 0
y = 0

value_amount = int(input())

for i in range(value_amount):
    n = input()
    li = n.split()
    judge()
    
print(str(x)+' '+str(y))
    
