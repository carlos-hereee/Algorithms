#!/usr/bin/python

import argparse

# find the maximum difference between the smallest and largest prices in the list of prices


def find_max_profit(prices):
    profit = prices[1] - prices[0]

    for price in prices[:-1]:
        # iterate from 1 to the n-1 element (we have no shorting
        # so we can only sell on the last element)
        for sell in prices[prices.index(price)+1:]:
            # iterate to end of prices
            if (sell - price) > profit:
                profit = sell - price

    return profit


print(f'prices ', find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
