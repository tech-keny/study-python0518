val = input().split()

for i in range(2):
    if len(val[i]) ==1:
        val[i] = '0'+'0'+val[i]
    if len(val[i]) ==2:
        val[i] = '0' +val[i]

x = int(val[0]) + int(val[1])
original = str(x)
count = 0
if len(str(x)) == 4:
    if int(val[0][2]) + int(val[1][2]) >= 10:
        x -=10
    if int(val[0][1]) + int(val[1][1]) >= 10:
        x -= 100
    if int(val[0][0]) +int(val[1][0]) >= 10:
        x -= 1000
    x = str(x) 
    if original[2] == '1' and int(val[0][1]) + int(val[1][1]) == 10 and int(original[1]) >1:
        x = '0' + x
    if original[1] == '1' and int(val[0][0]) + int(val[1][0]) == 10 :
        x = '0' +x
    print(x)
    
elif len(str(x)) == 3:
    if int(val[0][2]) + int(val[1][2]) >= 10:
        x -= 10
    if int(val[0][1]) + int(val[1][1]) >= 10:
        x -= 100
    x = str(x)
    if original[2] == '1' and int(val[0][1]) + int(val[1][1]) == 10:
        x = '0' +x
    print(x)
    
    
elif len(str(x)) ==2:
    if int(val[0][2]) + int(val[1][2]) >= 10:
        x -=10
    print(x)
else:
    print(x)