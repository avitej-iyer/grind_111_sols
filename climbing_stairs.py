class Solution:
    def climbStairs(self, n: int) -> int:
        # Turns out, the numberof ways to sum up to n using 1's and 2's 
        # follows the Fibonacci function as below:
        # n = 1 : 1 (1 way)
        # n = 2 : 1+1,2 (2 ways)
        # n = 3 : 1+1+1,1+2,2+1 (3 ways)
        # n = 4 : 1+1+1+1,1+2+1,2+2,2+1+1,1+1+2 (5 ways)
        # given this, the problem just becomes finding the nth fibonacci 

        def fibonacci(n):
            f = [0,1]
            for x in range(2, n+1):
                f.append(f[x-1] + f[x-2])
            return f[n]

        # 0th term is just 0, which won't be a case
        return fibonacci(n+1)