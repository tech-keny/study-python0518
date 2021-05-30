num = int(input())

x = input().split()

new = list(map(lambda a:x.count(a),x))


dl = {}

for i in range(num):
    dl[x[i]] = new[i]


max_val = max(dl.values())
keys_of_max_val = [key for key in dl if dl[key] == max_val]

keys_of_max_val = list(map(int,keys_of_max_val))

final_result = sorted(keys_of_max_val,reverse=False)

final_result = list(map(str, final_result))

print(' '.join(final_result))