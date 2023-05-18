class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = 99999
        for x in prices:
            if x < min_price: 
                min_price = x
                pass
            if x-min_price > max_prof:
                max_prof = x-min_price
        return max_prof 