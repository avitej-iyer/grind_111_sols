class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp_list = [False] * (len(s) + 1)
        dp_list[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp_list[j] and (s[j:i] in wordDict):
                    dp_list[i] = True
                    break
        
        return dp_list[-1]