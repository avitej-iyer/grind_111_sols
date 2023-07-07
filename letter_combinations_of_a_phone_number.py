class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = {"2" : "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []

        def back(comb, next):
            if not next:
                result.append(comb)
                return

            for _ in phone[next[0]]:
                back(comb + _, next[1:])

        back("", digits) 
        return result           



