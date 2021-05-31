num = input().split()

word_len = int(num[0])

states = num[2]
sta = num[1]

for count in range(word_len):
    if sta != states:
        states = states[1:] + states[0]
    else:
        print(count)
        break
    
