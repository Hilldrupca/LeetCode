
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:
    '''
    LeetCode Monthly Challenge problem for December 9th, 2020.
    
    Implement a binary search tree iterator class with hasNext(), and next()
    methods. This is not a standard implementation of a python iterator.
    '''
    def __init__(self, root: TreeNode):
        self.stack = []
        self.current_node = root
        self.prev_val = float('-inf')
        
        while root.right:
            root = root.right
            
        self.end = root.val
        
    def next(self) -> int:
        '''
        Returns the next inorder value of a binary search tree.
        '''
        if not self.hasNext():
            raise StopIteration
        
        node = self.current_node
        
        while node:
            self.stack.append(node)
            node = node.left
                
        next_node = self.stack.pop()
        self.current_node, self.prev_val = next_node.right, next_node.val
        
        return next_node.val
    
    def hasNext(self) -> bool:
        '''
        Returns whether the iterator has more nodes to visit.
        '''
        return self.prev_val < self.end
