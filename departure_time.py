time = list(map(int,input().split()))

house_hour = 0
house_min = 0


num = int(input())
for i in range(num):
    x = list(map(int,input().split()))
    dth = x[0]
    atm =  x[1] + time[1] + time[2] 
    ath = dth
    if atm >=60:
        atm -= 60
        ath +=1
    else:
        pass
    
    dtm =x[1] -time[0]
    if dtm <0:
        dtm = 60 + dtm
        dth -=1
    else:
        pass
    if ath <=8 and atm <=59:
        if dth > house_hour:
            house_hour = dth
            house_min = dtm
        elif dth == house_hour:
            if dtm > house_min:
                house_hour = dth
                house_min = dtm
            else:
                pass
        else:
            pass
    else:
        pass
    
if house_min < 0:
    print('0' + str(house_hour) + ':' +'0'+str(house_min))
else:
    print('0' + str(house_hour) + ':' +str(house_min))
        