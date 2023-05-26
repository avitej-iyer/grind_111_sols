class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for x in ransomNote:
            if x in magazine:
                magazine = magazine.replace(x,"",1)
            else:
                return False

        return True