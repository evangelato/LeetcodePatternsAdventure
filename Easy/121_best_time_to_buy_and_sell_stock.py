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
            if p < prices[beg]:
                beg = i
                end = i
                continue
            if p >= prices[end]:
                end = i
                if (p - prices[beg]) > max_profit:
                    max_profit = p - prices[beg]

        return max_profit
