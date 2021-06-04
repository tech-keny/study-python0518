num = int(input())


name_list=[]

time = []

time_table =[]

for i in range(num):
    x = input().split()
    name_list.append(x[0])
    time.append(int(x[1]))
    
sh = 10
sm = 0
eh = 10
em = 0
for j in range(num):
    if eh == 11:
        if em + 10 + time[j] >=61:
            sh = eh + 1
            sm = em
        elif em + 10 + time[j] == 60:
            sm = em +10
            if sm >= 60:
                sh = eh +1
                sm -=60
            else:
                sh = eh
        else:
            sh = eh
    elif eh ==10:
        if em > 50 and sm + time[j] >=61:
            sh = eh +1
            sm =em
    else:
        pass
    
    
    em = sm + time[j]
    eh = sh
    if em >=60:
        eh = sh + 1
        em -=60
    else:
        pass
    if sm <10:
        if em <10:
            time_table.append(str(sh)+':'+'0'+str(sm)+' '+'-'+' '+str(eh)+':'+'0'+str(em))
        else:
            time_table.append(str(sh)+':'+'0'+str(sm)+' '+'-'+' '+str(eh)+':'+str(em))
    else:
        if em <10:
            time_table.append(str(sh)+':'+str(sm)+' '+'-'+' '+str(eh)+':'+'0'+str(em))
        else:
            time_table.append(str(sh)+':'+str(sm)+' '+'-'+' '+str(eh)+':'+str(em)) 
    
    if eh != 11:
        sm = em + 10
        if sm >=60:
            sh = eh +1
            sm -= 60
        else:
            sh = eh
    else:
        pass
    
for k,l in zip(time_table,name_list):
    print(k,l)    