val = input().split()

for i in range(2):
    if len(val[i]) ==1:
        val[i] = '0'+'0'+val[i]
    if len(val[i]) ==2:
        val[i] = '0' +val[i]

if int(val[0][2]) + int(val[1][2]) >=10
    