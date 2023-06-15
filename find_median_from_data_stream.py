import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, -num))
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0] - self.min_heap[0])/2.0
        else:
            return float(self.max_heap[0])    