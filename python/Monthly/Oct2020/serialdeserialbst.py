from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def level_order(self) -> List[int]:
        '''Returns the level order of a binary search tree. Used for testing'''
        order = []
        bfs = deque([self])
        while bfs:
            node = bfs.popleft()
            if node:
                order.append(node.val)
            else:
                order.append(None)
                continue
                
            if node.left or node.right:
                bfs.append(node.left)
                bfs.append(node.right)
                
        return order
            
class Codec:
    '''
    LeetCode Monthly Challenge problem for October 9th, 2020.
    '''
    def serialize(self, root: TreeNode) -> str:
        '''
        Serializes a binary search tree into preorder traversal order.
        
        Params:
            root - The root node of a binary search tree.
            
        Returns:
            str - A string representation of the preorder traversal of a binary
                  search tree.
                  
        Example:
            Given The following tree, t:
            
                        3
                       / \
                      1   4
                       \
                        2
            
            serialize(t)   ->   '3,1,2,4'
        '''
        if not root:
            return ''
        
        preorder = []
        def build_preorder(node):
            if node:
                preorder.append(str(node.val))
                build_preorder(node.left)
                build_preorder(node.right)
                
        build_preorder(root)
        
        return ','.join(preorder)
    
    
    def deserialize(self, data: str) -> TreeNode:
        '''
        Deserializes and reconstructs a binary search tree.
        
        Params:
            data - A string representation of the preorder traversal of a
                   binary search tree.
                   
        Returns:
            TreeNode - The root node of a binary search tree. Original
                       structure preserved.
                       
        Example:
            deserialize('3,1,2,4') returns the following tree:
            
                        3
                       / \
                      1   4
                       \
                        2
        '''
        if not data:
            return
        
        data = data.split(',')
        self.idx = 0
        
        def tree_builder(lower, upper):
            if self.idx >= len(data):
                return None
            
            num = int(data[self.idx])
            root = None
            
            if lower < num < upper:
                root = TreeNode(num)
                self.idx += 1
                root.left = tree_builder(lower, num)
                root.right = tree_builder(num, upper)
                    
            return root
        
        return tree_builder(float('-inf'), float('inf'))
