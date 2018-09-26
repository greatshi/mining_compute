#!/usr/bin/env python
#coding=utf-8

BTC_PRICE = 45000
BTC_PER_HASH = 0.00003409
HASH_RATE = 13.5
round = 13
hard = 0.93
KW = 1.3
electric = 0.3
fee = KW * 24 * 13 * electric

def easy_mode():
    daily_earn = BTC_PER_HASH * HASH_RATE * BTC_PRICE
    daily_cost = KW * 24 * electric
    print('daily_earn: {}'.format(daily_earn))
    print('daily_cost: {}'.format(daily_cost))
    print('real_earn: {}'.format(daily_earn - daily_cost))


def range_mode():
    earn = 0
    cost = 0
    for i in range(0, 100):
        round_mine = BTC_PER_HASH * HASH_RATE * round * (hard ** i)
        earn += round_mine
        cost += fee
        earn -= fee/float(BTC_PRICE)
        if round_mine <= fee/float(BTC_PRICE):
            print('{} month'.format(i*13/30.0))
            break
        if i == 99:
            print('{} month'.format(i*13/30.0))
        print('round: {}, earn: {}, money: {}, total: {}'.format(
              i+1, earn, round_mine*BTC_PRICE, earn*BTC_PRICE))
    print('earn: {} cost: {}'.format(earn, cost))


def main():
    range_mode()
    easy_mode()

if __name__ == '__main__':
    main()
