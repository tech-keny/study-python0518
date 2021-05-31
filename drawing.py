size = list(map(int, input().split()))

sl = list(map(int, input().split()))

x = (size[0]*abs(sl[1]))+(size[1]*abs(sl[0])) - abs(sl[0]*sl[1])

print(x)