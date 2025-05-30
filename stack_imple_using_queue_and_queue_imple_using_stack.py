from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[len(self.q)-1]

    def empty(self) -> bool:
        return len(self.q) == 0
s = MyStack()
s.push(19)
s.empty()
print(s.pop())
###### queue implementation
class MyQueue:

    def __init__(self):
        self.s = deque()
        self.p = deque()

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        self.peek()
        return self.p.pop()

    def peek(self) -> int:
        if not self.p:
            while self.s:
                self.p.append(self.s.pop())
        return self.p[-1]

    def empty(self) -> bool:
        return len(self.s) == 0 and len(self.p) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(10)
print(obj.pop())