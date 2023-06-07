class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for x in range(target+1)]
        
        for number in candidates:
            for x in range(number, target+1):
                if x == number: dp[x].append([number])
                for comb in dp[x-number]: dp[x].append(comb + [number])

        return dp[-1]        
