num = int(input())

x = input().split()

new = list(map(lambda a:x.count(a),x))

dl = {}

for i in range(num):
    dl[x[i]] = new[i]
    

max_val = max(dl.values())
keys_of_max_val = [key for key in dl if dl[key] == max_val]

print(' '.join(keys_of_max_val))