
BTC_PRICE = 51500
BTC_PER_HASH = 0.00006376
HASH_RATE = 13.5
round = 13
hard = 0.92
KW = 1.4
fee = KW * 24 * 13 * 0.3
earn = 0
cost = 0
for i in range(0, 100):
    round_mine = BTC_PER_HASH * HASH_RATE * round * (hard ** i)
    earn += round_mine
    cost += fee
    # earn -= fee/float(BTC_PRICE)
    # if round_mine <= fee/float(BTC_PRICE):
        # print str(i*13/30.0) + 'month'
        # break
    if i == 99:
        print str(i*13/30.0) + 'month'
    print  str(i + 1), str(earn), str(round_mine * BTC_PRICE), str(earn * BTC_PRICE)
print 'earn: ' + str(earn) + ' cost: ' + str(cost)
print '51500 * earn: '+ str(BTC_PRICE * earn)
