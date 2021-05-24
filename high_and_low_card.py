# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
pn = input()
card = int(input())
pl = pn.split()

for i in range(card):
    x = input()
    li = x.split()
    if int(pl[0]) > int(li[0]):
        print('High')
    elif int(pl[0]) == int(li[0]):
        if int(pl[1]) < int(li[1]):
            print('High')
        else:
            print('Low')
    else:
        print('Low')
    
