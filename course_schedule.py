class Solution:
    # generate an adjacency list such that you 
    # append the courses you can take once you take a certain course
    def gen_adj_list(self, numCourses, prerequisites):
            adjList = [[] for _ in range(numCourses)]
            for a,b in prerequisites:
                adjList[b].append(a)
            return adjList

    def topoSortBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        new_adj_list = self.gen_adj_list(numCourses, prerequisites)
        inDeg = [0]*numCourses

        for a,b in prerequisites:
            inDeg[a] += 1

        new_queue = []
        for x in range(numCourses):
            if inDeg[x] == 0:
                new_queue.append(x)

        count = 0
        sorted_list = []

        while new_queue:
            top_node = new_queue.pop(0)
            sorted_list.append(top_node)
            count+=1

            for descendant in new_adj_list[top_node]:
                inDeg[descendant] -= 1
                if inDeg[descendant] == 0:
                    new_queue.append(descendant)

        if count != numCourses: return None
        else: return sorted_list
                      
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return bool(self.topoSortBFS(numCourses, prerequisites)) 