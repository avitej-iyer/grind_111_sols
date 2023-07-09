from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_dict = Counter(s[:len(p) - 1])
        p_dict = Counter(p)

        start = 0
        res = []

        for i in range(len(p) - 1, len(s)):
            s_dict[s[i]] += 1

            if s_dict == p_dict : res.append(start)

            s_dict[s[start]] -= 1

            if s_dict[s[start]] == 0:
                del s_dict[s[start]]
            start+= 1

        return res    

                




