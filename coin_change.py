class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_list = [0] + [999999 for i in range(amount)]
        for i in range(1,1+amount):
            for x in coins:
                if i >= x:
                    dp_list[i] = min(dp_list[i], dp_list[i-x] + 1)
        if dp_list[-1] == 999999:
            return -1
        return dp_list[-1]                 