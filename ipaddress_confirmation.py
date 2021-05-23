def judge():
    for j in range(len(li)):
        global count
        if int(li[j]) <0 or 255<int(li[j]):
            print('False')
            break
        else:
            count += 1
            



a = int(input())

for i in range(a):
	x = input()
	li = x.split('.')
	if len(li) == 4 and "''" in li:
		print('False')
	elif len(li) ==4 and "''" not in li:
	    count = 0
	    judge()
	    if count ==4:
	        print('True')
	else:
		print('False')

