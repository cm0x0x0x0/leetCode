class MyQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
        self.size = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        self.shift()
        self.size -= 1
        return self.stack2.pop()

    def peek(self) -> int:
        self.shift()
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return self.size == 0

    def shift(self) -> None:
        if len(self.stack2) == 0:
            for i in range(self.size):
                self.stack2.append(self.stack1.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()