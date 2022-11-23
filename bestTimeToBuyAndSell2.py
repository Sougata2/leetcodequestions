def buy_and_sell(prices):
    profit = 0
    for i in range(len(prices)-1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]

    return profit


if __name__ == "__main__":
    print(buy_and_sell([7, 1, 5, 3, 6, 4]))
    print(buy_and_sell([1, 2, 3, 4, 5]))
    print(buy_and_sell([7, 6, 4, 3, 1]))
