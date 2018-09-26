
LTC_PRICE = 780
LTC_PER_HASH = 0.00004781
HASH_RATE = 220
round = 3
hard = 0.97
KW = 2
fee = KW * 24 * 3 * 0.25/float(LTC_PRICE)
earn = 0
for i in range(0, 300):
    round_mine = LTC_PER_HASH * HASH_RATE * round * (hard ** i)
    earn += round_mine
    earn -= fee
    if round_mine <= fee:
        print str(i*3/30.0) + 'month'
        break
    print  str(i + 1), str(earn), str(round_mine * LTC_PRICE), str(earn * LTC_PRICE)
