from typing import List

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
        
class Solution:
    def postorder(self, root: Node) -> List[int]:
        '''
        Returns the postorder traversal of an n-ary tree.
        
        Params:
            root - The root node of an n-ary tree.
            
        Returns:
            List[int] - The postorder traversal.
            
        Examples:
            Given the following n-ary tree, a:
                    1
                   /|\
                  3 2 4
                 / \
                5   6
                
            postorder(a)   ->   [5,6,3,2,4,1]
            
            Given the following n-ary tree, b:
                ____1_____
               /   / \    \
              /   /   \    \
             2   3     4    5
                / \    |   / \
               6   7   8  9   10
                   |   |  |
                  11  12  13
                   |
                  14
                  
            postorder(b)   ->   [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
        '''
        if root is None:
            return []
        
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node.val)
            stack.extend(node.children)
            
        return order[::-1]
