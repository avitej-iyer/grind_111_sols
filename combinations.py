class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def track(first, curr):
            if len(curr) == k:
                output.append(curr[:])
                return
            for x in range(first, n+1):
                curr.append(x)
                track(x+1, curr)
                curr.pop()
        output = []
        track(1, [])
        return output        