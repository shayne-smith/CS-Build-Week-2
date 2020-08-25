class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        copy = []
        while len(self.stack) > 0:
            copy.append(self.stack.pop())
        
        answer = copy.pop()
        
        while len(copy) > 0:
            self.stack.append(copy.pop())
        
        return answer
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        copy = list.copy(self.stack)
        
        while len(copy) > 1:
            copy.pop()
        return copy[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()