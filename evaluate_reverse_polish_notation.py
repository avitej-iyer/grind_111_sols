class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # taking the stack approach for this one
        stack = []

        # faster lookup with sets
        operators = set(("+","-","*","/"))


        for x in tokens:

            # basically, for every token in the given list you either append it to the stack
            # or it is a operator, in which case you operate on the preceding two elements.
            # The pop clears out the first element and assigns the operated value to 
            # the second.       
            if x not in operators:
                stack.append(int(x))
            else:
                first_operator = stack.pop()
                if x == "+" : stack[-1] = stack[-1] + first_operator
                if x == "-" : stack[-1] = stack[-1] - first_operator
                if x == "*" : stack[-1] = stack[-1] * first_operator
                if x == "/" : stack[-1] = int(stack[-1] / first_operator)

        return stack[0]   