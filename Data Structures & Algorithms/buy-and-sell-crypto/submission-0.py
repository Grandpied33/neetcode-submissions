class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        best_profit = 0

        for price in prices:
            if price <lowest:
                lowest = price
            current_profit = price - lowest
            if current_profit >best_profit :
                best_profit=current_profit
        return best_profit