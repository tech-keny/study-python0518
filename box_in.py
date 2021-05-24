# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
sl = input_line.split()

m = int(sl[1])*2

for n in range(1,int(sl[0])+1):
    x = input()
    li = x.split()
    h = int(li[0])
    w = int(li[1])
    d = int(li[2])
    new_list = [h,w,d]
    if m <= min(new_list):
        print(n)
    