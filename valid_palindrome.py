class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for x in s:
            downsized = x.lower()
            if 48<=ord(downsized)<=57 or 97<=ord(downsized)<=122:
                new_str += downsized    
        return (new_str == new_str[::-1])