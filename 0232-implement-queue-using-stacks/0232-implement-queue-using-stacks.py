class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        if len(self.s2)!=0 :
            x=self.s2[-1]
            self.s2.pop()
        else:
            for i in range(len(self.s1)):
                self.s2.append(self.s1[-1])
                self.s1.pop()
            x=self.s2[-1]
            self.s2.pop()
        return x
    
    def peek(self) -> int:
        if len(self.s2)==0 : return self.s1[0]
        else : return self.s2[-1]

    def empty(self) -> bool:
        if (len(self.s1) + len(self.s2))==0 : return True
        else : return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()