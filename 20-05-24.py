"""
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""


def max_profit(stock_prices): 

    if not stock_prices:
        return 0

    min_price = stock_prices[0]
    max_profit = 0

    for price in stock_prices:

        if price < min_price:
            min_price = price

        pot_profit = price - min_price
    
        if pot_profit > max_profit:
            max_profit = pot_profit

    return max_profit


print(max_profit([9, 11, 8, 5, 7, 10]))