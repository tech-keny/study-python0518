# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def judge():
    global count
    for j in range(6):
        if li[j] in wn:
            count += 1
        


winning_number = input()
wn = winning_number.split()

paper = int(input())

for i in range(paper):
    x = input()
    li = x.split()
    count = 0
    judge()
    print(count)



