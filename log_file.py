val = input().split('.')
# print(val)
argument = []
for o in range(2,4):
    if '-' in val[o]:
        argument.append(int(val[o][1:val[o].index('-')]))
        argument.append(int(val[o][val[o].index('-')+1:val[o].index(']')]))
        val[o] = argument

# print(val)

num = int(input())

original = []

li = []

result = []

for i in range(num):
    x = input()
    pre_result = x
    index = x.index('-')
    pre_result = pre_result.split()
    pre_result = pre_result[0] +' ' + pre_result[3]+' ' + pre_result[6]
    pre_result = pre_result.replace('[','')
    original.append(pre_result)
    x = x[:index-1]
    x = x.split('.')
    # print(x)
    li.append(x)



count = 0
for j in range(num):
    for k in range(4):
        if val[k] == li[j][k]:
            count += 1
        elif val[k] == '*' :
            for m in range(256):
                if int(li[j][k]) ==m:
                    count += 1
                else:
                    pass
        elif type(val[k]) == list :
            for l in range(val[k][0],val[k][1]+1):
                if int(li[j][k]) == l:
                    count += 1
                else:
                    pass
    if count == 4:
        result.append(original[j])
        count = 0
    else:
        count = 0

# print(original)
for n in result:
    print(n)

                
            