class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # if the end is not reachable because it doesn't exist in the wordList
        if endWord not in wordList:
            return 0
        
        word_len = len(beginWord)
        
        # using a mapping approach here - we're building a "neighour" matrix with the keys 
        # being possible ofshoots of a word (for ex. "hot" -> "*ot", "h*t", "ho*")

        # we're gonna add the beginWord to wordList first so it can be included in the 
        # matrix generation
        neighbours = collections.defaultdict(list)
        wordList.append(beginWord)

        # matrix generation step from above
        for word in wordList:
            for x in range(word_len):
                neighbours[word[:x] + "*" + word[x+1:]].append(word)

        # so we don't revisit nodes during "BFS"
        visited_nodes = set([beginWord])

        # so we keep going from neighbour to neighbour
        curr_queue = deque([beginWord])       

        res = 1

        while curr_queue:
            for i in range(len(curr_queue)):
                word = curr_queue.popleft()

                if word == endWord:
                    return res
                
                for j in range(word_len):
                    for neighbour_word in neighbours[word[:j] + "*" + word[j+1:]]:
                        if neighbour_word not in visited_nodes:
                            visited_nodes.add(neighbour_word)
                            curr_queue.append(neighbour_word)
            res += 1


        return 0


