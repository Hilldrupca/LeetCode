from typing import List

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
        
class Solution:
    def preorder(self, root: Node) -> List[int]:
        '''
        Rturns the preorder traversal of an n-ary tree.
        
        Params:
            root - The root node of an n-ary tree.
            
        Returns:
            List[int] - The preorder traversal of the tree.
            
        Examples:
            Given the following n-ary tree, a:
                    1
                   /|\
                  3 2 4
                 / \
                5   6
                
            postorder(a)   ->   [1,3,5,6,2,4]
            
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
                  
            postorder(b)   ->   [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
        '''
        if root is None:
            return []
        
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node.val)
            stack.extend(node.children[::-1])
            
        return order
