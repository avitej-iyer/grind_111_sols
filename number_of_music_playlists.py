class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @lru_cache(None)
        def dp(uni, rep, rem, STNR):
            if STNR == 0: 
                rep += 1
                STNR = 1
            if uni > rem : 
                return 0
            if rem == 0:
                return 1
            
            res = 0
            if uni > 0:
                res += dp(uni-1, rep, rem-1,STNR-1) * uni
            if rep > 0:
                res += dp(uni, rep-1, rem-1, STNR-1) * rep
            return res
        
        return dp(n,0,goal, k+1) % (10**9 + 7)