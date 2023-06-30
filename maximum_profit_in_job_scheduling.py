class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(startTime[x], endTime[x], profit[x]) for x in range(len(profit))])
        heap = []
        cur_profit = max_profit = 0

        for beg, end, prof in jobs:
            while heap and heap[0][0] <= beg:
                et, temp = heapq.heappop(heap)
                cur_profit = max(cur_profit, temp)
            heapq.heappush(heap, (end, cur_profit+prof)) 
            max_profit = max(max_profit, cur_profit+prof)

        return max_profit    

