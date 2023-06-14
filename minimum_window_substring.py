class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # leaving it as counter objects and not dicts
        # because of comparison below
        s_dict, t_dict = collections.Counter(), (collections.Counter(t))

        # defining a "slow" pointer here, fast pointer is the 
        # loop iterator variable
        l, results = 0, ""

        for r in range(len(s)):
            s_dict[s[r]] += 1

            # the & operator between two counter objects gives the 
            # intersection of objects
            # use this to shrink the window as needed
            while (s_dict & t_dict == t_dict):
                if len(s[l:r+1]) < len(results) or results == "":
                    results = s[l:r+1]
                s_dict[s[l]] -= 1
                l+= 1

        return results            




    
        






        


