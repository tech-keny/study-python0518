# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！
def divisor():
    global n
    if x % j == 0:
        n += j

def result():
    if s == x:
        print('perfect')
    elif abs(x-s) == 1:
        print('nearly')
    else:
        print('neither')
        

t = int(input())

for i in range(t):
    x = int(input())
    n = 0
    for j in range(1, x+1):
        divisor()
    s = n - x
    result()
        
    