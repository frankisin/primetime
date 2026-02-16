def maxProfit(prices):
    min_value = float('inf')

    max_profit = 0 

    for price in prices: #O(N) 
        if price < min_value: #O(C)
            min_value = price 
        
        profit = price - min_value #O(C)

        if profit > max_profit: #O(C)
            max_profit = profit
    return max_profit 


