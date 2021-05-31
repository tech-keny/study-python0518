num = list(map(int,input().split()))

f1 = num[0]

a_bud = num[1]

b_bud = num[2]

bid_price = f1

while bid_price <= max(num):
    if bid_price +1010 > b_bud and bid_price +10 <= a_bud:
        print('A'+ ' ' + str(bid_price+10))
        break
    else:
        bid_price += 10
    if bid_price +1010 >a_bud and bid_price +1000 <=b_bud:
        print('B' + ' ' + str(bid_price+1000))
        break
    else:
        bid_price += 1000
    