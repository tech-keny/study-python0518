# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math 

def calc():
    global point_total
    if '5' in li[0]:
        point = math.floor(int(li[1])*0.05)
        point_total += point
    elif '3' in li[0]:
        point = math.floor(int(li[1])*0.03)
        point_total += point
    else:
        point = math.floor(int(li[1])*0.01)
        point_total += point
        
        
        
    

days = int(input())


point_total = 0
for i in range(days):
    x = input()
    li = x.split()
    calc()
print(point_total)
