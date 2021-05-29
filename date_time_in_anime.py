days = input().split()


d = days[0].split('/')

t = days[1].split(':')

x = int(t[0]) // 24 

d[1] = int(d[1]) + x

t[0] = int(t[0]) -24*x

print(str(d[0])+'/'+str(d[1])+' '+format(t[0],'02')+':'+str(t[1]))