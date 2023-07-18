class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret_len = 0
        last_char = False # false is space, true is char
        for x in range(len(s)-1, -1, -1):
            if s[x] is not " ":
                ret_len += 1
                last_char = True
            if s[x] is " " and last_char == True:
                break

        return ret_len    


            