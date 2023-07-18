import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(str)
        for x in strs:
            letter_count = tuple(sorted(collections.Counter(x).items()))
            if letter_count not in anagrams:
                anagrams[letter_count] = [x]
            else:
                anagrams[letter_count] += [x]
        print(anagrams)

        return [values for values in anagrams.values()]        
