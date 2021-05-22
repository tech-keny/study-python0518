# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
milimeters = input("距離を入力してください:")

ns = milimeters.split()




if ns[1] == "km":
    x = int(ns[0])*1000000
elif ns[1] == "cm":
    x = int(ns[0])*10
elif ns[1] == "m":
    x = int(ns[0])*1000
else:
    x = int(ns[0])*1

print(x)













