# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def judge():
    if int(cl[2])**2 <= (int(li[0])-int(cl[0]))**2 + (int(li[1])-int(cl[1]))**2 <= int(cl[3])**2:
        print('yes')
    else:
        print('no')

circle = input()
cl = circle.split()
people = int(input())

for i in range(people):
    x = input()
    li = x.split()
    judge()