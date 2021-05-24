# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def calc():
    global count
    if al[0] in dl:
        count += 1
        if int(al[1]) >= dl[al[0]]:
            x = int(al[1]) // dl[al[0]]
            li.append(x)
        else: 
            pass
    else:
        pass
    

recipe = int(input())

dl = {}

for i in range(recipe):
    f = input()
    fl = f.split()

    dl[fl[0]] = int(fl[1])

amount = int(input())

li = []
count = 0
for j in range(amount):
    a = input()
    al = a.split()
    
    calc()
if not li:
    print(0)
elif count != recipe:
    print(0)
if count == recipe:
    print(min(li))
   

    