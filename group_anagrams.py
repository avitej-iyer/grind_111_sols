import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(str)
        for x in strs:
            # you could alternatively jus tuse the sorted word
            # as the key, would probably cut down on runtime for small words
            letter_count = tuple(sorted(collections.Counter(x).items()))
            if letter_count not in anagrams:
                anagrams[letter_count] = [x]
            else:
                anagrams[letter_count] += [x]
        print(anagrams)

        return [values for values in anagrams.values()]        
