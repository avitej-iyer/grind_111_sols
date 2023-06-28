class Solution:
    def calculate(self, s: str) -> int:
        curr_num, stack, sign, res = 0, [], 1, 0

        for char in s:
            
            if char.isdigit():
                # also takes care of if the number "continues"
                curr_num = curr_num*10 + int(char)

            elif char in ("+", "-"):
                # first adding our original value to result
                res += curr_num*sign
                # preparing for next operand
                sign = -1 if char == "-" else 1
                curr_num = 0

            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0 
                sign = 1

            elif char ==")":
                res += curr_num*sign
                res *= stack.pop()
                res += stack.pop()
                curr_num = 0

        return res + curr_num*sign      


    