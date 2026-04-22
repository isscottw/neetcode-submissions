class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n) Space: O(1)
        profit, buy_day, sell_day = 0, 0, 1

        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                profit = max(profit, prices[sell_day] - prices[buy_day])
            else:
                buy_day = sell_day
            sell_day += 1
        return profit
