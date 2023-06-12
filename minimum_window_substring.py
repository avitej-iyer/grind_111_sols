def minWindow(s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        fast, slow = 0, -1

        t_dict={}
        s_dict={}

        # initial hashmap contruction for keeping track of letter counts in t
        for x in t:
            if x in t_dict:
                t_dict[x] += 1
            else:
                t_dict[x] = 1
        
        ans = "1"

        while fast > slow and fast < len(s):

            if s[fast] in s_dict:
                s_dict[s[fast]] += 1
            else:
                s_dict[s[fast]] = 1

            print("Outer : ", s_dict)
            
            while t_dict.items() <= s_dict.items():
                if ans == "1":
                    ans = s[slow:fast+1]
                else:    
                    ans = min(ans, s[slow:fast+1], key = len)

                print(ans)
                
                s_dict[s[slow]] -= 1
                print("Inner : ", s_dict)
                slow += 1
            
            fast += 1

        return ans

minWindow("ADOBECODEBANC", "ABC")