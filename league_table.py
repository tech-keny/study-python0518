num = int(input())
win = []
lose = []
for i in range(num*(num-1)//2):
    s = list(map(int,input().split()))
    win.append(s[0])
    lose.append(s[1])
    
# score = [list(map(int,input().split())) for i in range(num*(num-1)//2)]

score = [list('-')*num for j in range(num)]


# print(score)
    
for a,b in zip(win,lose):
    score[a-1][b-1] = 'W'
    score[b-1][a-1] = 'L'
 
board ='\n'.join(map(' '.join, score))
print(board)
