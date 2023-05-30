class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        for x in s:
            if x not in char_set:
                char_set.add(x)
            else:
                char_set.remove(x)
        if len(char_set) is not 0:
            return len(s) - len(char_set) + 1
        else: return len(s) 