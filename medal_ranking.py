data = int(input())
score = [list(map(int,input().split())) for i in range(data)]

print(score)

score.sort(key=lambda x:(x[0],x[1],x[2]))
score.reverse()

for s in score:
    print(*s)