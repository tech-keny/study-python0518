# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
li = input_line.split()

nl = [int(li[0]),float(int(li[1])/100),float(int(li[2])/100)]

remain = nl[0]-(nl[0]*nl[1])
result = remain -(remain*nl[2])
print(result)

