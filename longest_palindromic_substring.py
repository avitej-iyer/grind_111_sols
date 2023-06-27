class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_len = len(s)

        # constructing our dp table, initialize eveything to false
        dp_table = [[False]*string_len for _ in range(string_len)]

        # indices of longest discovered palindrome
        ans = [0,1]

        # a character by itself is a palindrome
        for x in range(string_len):
            dp_table[x][x] = True

        for i in range(string_len-1,-1,-1):
            # j starts AFTER i so we only deal with the top half of the dp table
            for j in range(i+1, string_len):
                
                # if the extremities match : ex "A""bcb""A"
                if s[i] == s[j]:
                    # we check if the inner string (in the above example, "bcb") matches
                    # of if it's one character, in which case it's a palindrome
                    if dp_table[i+1][j-1] or j-i == 1:
                        dp_table[i][j] = True
                        # keeping track of longest palindrome
                        if (j + 1 - i > ans[1] - ans[0]):
                            ans[0], ans[1] = i,j+1

        return s[ans[0] : ans[1]]                    