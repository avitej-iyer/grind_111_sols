class Solution:
    def isValid(self, s: str) -> bool: 
        new_stack = []
        stack_size = 0
        for x in s:
            if stack_size == 0:
                if x not in [")","}","]"]:
                    new_stack += x
                    stack_size += 1
                else:
                    return False
            else:
                if x in ["(","{","["]:
                    new_stack += x
                    stack_size += 1
                else:
                    if x == ")":
                        if new_stack[stack_size-1] != "(":
                            return False
                        else:
                            new_stack.pop()
                            stack_size -= 1    
                    if x == "}":
                        if new_stack[stack_size-1] != "{":
                            return False
                        else:
                            new_stack.pop()
                            stack_size -= 1  
                    if x == "]":
                        if new_stack[stack_size-1] != "[":
                                return False
                        else:
                            new_stack.pop()
                            stack_size -= 1 
        if stack_size != 0:
            return False                    
        return True                                  
