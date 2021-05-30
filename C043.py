num = int(input())

x = input().split()

print(x)

new = list(map(lambda a:x.count(a),x))

dl = {}

for i in range(num):
    dl[x[i]] = new[i]
    
print(dl)

max_val = max(dl.values())
print(max_val)
keys_of_max_val = [key for key in dl if dl[key] == max_val]
# result = max(dl, key=dl.get)
print(' '.join(keys_of_max_val))