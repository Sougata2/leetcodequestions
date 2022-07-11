def stock_picker(lst):
    """
    Calculate the maximum profit one can achieve from this transaction.
    if you cannot achieve any profit then return 0.

    :param lst:
    :return: int
    """
    buy = 0
    profit = 0
    got_buy_price = False
    for i in range(len(lst) - 1):
        if lst[i + 1] > lst[i]:
            sell = lst[i + 1]
            if got_buy_price:
                if lst[i] < buy:
                    buy = lst[i]
            else:
                buy = lst[i]
                profit = sell - buy
                got_buy_price = True
            profit = max(profit, sell - buy)
    return profit


if __name__ == '__main__':
    print(stock_picker([7, 1, 5, 3, 6, 4]))
    print(stock_picker([7, 6, 4, 3, 1]))
