"""
Best time to buy and sell stock.

Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
--------
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for i in range(1,len(prices)):
            todays_price = prices[i]
            if todays_price < buy_price:
                buy_price = todays_price
                continue
            profit = max(profit,todays_price - buy_price)
        return profit
"""
Start with a profit of 0. Initially you can only buy the stock on the first day.

If at any time the current day's price is cheaper than the previously consider purchase date, set the 
current stocks price to the buy price. But don't update profit (you can't anyways if today).

Otherwise, the profit is the max between the past max profit and the current price minus the buy price.

"""