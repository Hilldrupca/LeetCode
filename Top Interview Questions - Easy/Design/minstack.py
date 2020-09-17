
class MinStack:
    '''
    A stack design whose methods perform in constant time.
    '''
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, x: int) -> None:
        '''
        Push element onto stack.
        '''
        self.stack.append(x)
        if self.min:
            self.min.append(min(self.min[-1], x))
        else:
            self.min.append(x)
            
    def pop(self) -> None:
        '''
        Removes the element on top of stack.
        '''
        if self.stack:
            del self.stack[-1]
            del self.min[-1]
            
    def top(self) -> int:
        '''
        Get the top element.
        '''
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        '''
        Get the minimum element in the stack.
        '''
        if self.min:
            return self.min[-1]
