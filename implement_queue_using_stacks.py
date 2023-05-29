class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            self.move()
        return self.out_stack.pop()    

    def peek(self) -> int:
        if not self.out_stack:
            self.move()
        return self.out_stack[-1]    

    def empty(self) -> bool:
        return not len(self.in_stack) and not len(self.out_stack)

    def move(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())