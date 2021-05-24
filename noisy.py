# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
position = input()
count = int(input())

pl = position.split()

for i in range(count):
    x = input()
    li = x.split()
    result = (int(li[0])-int(pl[0]))**2 + (int(li[1])-int(pl[1]))**2 - int(pl[2])**2
    if result >= 0:
        print('silent')
    else:
        print('noisy')
    


