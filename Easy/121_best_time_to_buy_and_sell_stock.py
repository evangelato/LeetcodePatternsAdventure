class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        beg = -1
        end = -1

        for i, p in enumerate(prices):
            if i == 0:
                beg = 0
                end = 0
                continue
            if prices[i] < prices[beg]:
                beg = i
                end = i
                continue
            if prices[i] >= prices[end]:
                end = i
                if (prices[end] - prices[beg]) > max_profit:
                    max_profit = prices[end] - prices[beg]

        return max_profit
