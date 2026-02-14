def maxProfit(prices):
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit
    return max_profit if max_profit > 0 else 0

prices = [7,1,5,3,6,4]

print(maxProfit(prices))



    
