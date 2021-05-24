# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def score_judge():
    global total
    for j in range(int(pl[0])):
        # number = round(int(li[j]))*(float(ol[j]))
        number = int(li[j])*float(ol[j])
        total += number
        
    
parameter = input()
point = input()
pl = parameter.split()
ol = point.split()

gl =[]
for i in range(int(pl[1])):
    x = input()
    li = x.split()
    total = 0
    score_judge()
    gl.append(total)
        

new_list = sorted(gl, reverse=True)
for h in range(int(pl[2])):
    print(round(new_list[h]))

