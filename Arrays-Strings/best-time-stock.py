"""Best Time to Buy and Sell Stock
Problem : Best Time to Buy and Sell Stock
Source   : LeetCode #121  |  Striver A2Z — Step 3 Arrays
Topic    : Sliding Window / Greedy
Difficulty: Easy
Date     : 2026-05-24

Approach:
  Track the minimum price seen so far (best day to buy).
  At each day, calculate profit = current price - min_price.
  Update max_profit if this profit is better.
  Never look back — one pass is enough.

  Key insight: you don't need two pointers explicitly.
  min_price acts as the left pointer, current index as right.

Time  : O(n)
Space : O(1)
"""
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

# Test cases
# maxProfit([7,1,5,3,6,4])  -> 5   (buy at 1, sell at 6)
# maxProfit([7,6,4,3,1])    -> 0   (prices only fall, no profit)
# maxProfit([2,4,1])        -> 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_price to infinity so any first day price will be lower than it.
        # This tracks the lowest buying price we have seen so far as we move left-to-right.
        min_price = float('inf')
        
        # Initialize max_profit to 0. If no profit can be made, we will return 0.
        max_profit = 0
        
        # Loop through each day's price exactly once (O(n) time complexity)
        for price in prices:
            
            # Condition 1: Check if today's price is the lowest we've seen so far.
            # If it is, we update our min_price (we'd ideally want to buy here).
            if price < min_price:
                min_price = price
                
            # Condition 2: If today's price isn't a new low, see how much profit
            # we would make by selling today (today's price minus the lowest historical price).
            # If this profit is greater than our record so far, update max_profit.
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        # Return the ultimate maximum profit found during the single pass
        return max_profit
