def max_profit(prices):
    buy_price = 0
    profit = float('-inf')
    for price in prices:
        buy_price = min(buy_price, price)
        profit = max(profit, price - buy_price)

    return profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([7, 6, 4, 3, 1]))
    print(max_profit([3, 2, 6, 5, 0, 3]))
