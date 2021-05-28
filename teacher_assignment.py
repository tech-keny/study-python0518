num = input().split()

if num[0] == 'x':
    if num[1] =='+':
        print(int(num[4]) - int(num[2]))
    else:
        print(int(num[4]) + int(num[2]))
        
elif num[2] == 'x':
    if num[1] =='+':
        print(int(num[4]) - int(num[0]))
    else:
        print(int(num[0]) - int(num[4]))
        
elif num[4] =='x':
    if num[1] =='+':
        print(int(num[0]) + int(num[2]))
    else:
        print(int(num[0]) - int(num[2]))