class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q)-1):
            self.q.append(self.q[0])
            self.q.popleft()

    def pop(self) -> int:
        x=self.q[0]
        self.q.popleft()
        return x

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        if len(self.q)==0 : return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()