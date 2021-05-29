f = input().split()
f = list(map(int, f))
s = input().split()
s = list(map(int, s))



x = input().split()
x = list(map(int,x))


win_first = 0
win_second = 0
if x[f[0]-1] < x[f[1]-1]:
    win_first = f[0]
else:
    win_first = f[1]

if x[s[0]-1] > x[s[1]-1]:
    win_second = s[1]
else:
    win_second = s[0]
    
sc = input().split()
sc = list(map(int, sc))

if win_first > win_second:
    if sc[0] > sc[1]:
        print(win_first)
        print(win_second)
    else:
        print(win_second)
        print(win_first)

if win_first < win_second:
    if sc[0] > sc[1]:
        print(win_second)
        print(win_first)
    else:
        print(win_first)
        print(win_second)




