# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
dislike = input()
amount = int(input())

count = 0
for i in range(amount):
    x = input()
    if dislike not in x:
        print(x)
    else:
        count += 1
        
if count == amount:
    print('none')