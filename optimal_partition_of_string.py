class Solution:
    def partitionString(self, s: str) -> int:
        char_set = set()
        i, ret = 0,0
        while i < len(s):
            ret += 1
            while i < len(s) and s[i] not in char_set:
                char_set.add(s[i])
                i += 1
            char_set.clear()
        return ret        
