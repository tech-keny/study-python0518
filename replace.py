# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
word = input()
li =[]
for i in range(len(word)):
    li.append(word[i])


dl = {'A':'4','E':'3','G':'6','I':'1','O':'0','S':'5','Z':'2'}

for j in range(len(word)):  
    if li[j] in dl:
            # li.replace(li[j],dl[li[j]])は指定できない（replaceメソッドがない）
            li[j] = dl[li[j]]

new_list = ''.join(li)
print(new_list)
        


