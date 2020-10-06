from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def level_order(self):
        '''Used to test correct insertion'''
        order = []
        bfs = deque([self])
        
        while bfs:
            node = bfs.popleft()
            if node:
                order.append(node.val)
            else:
                # Nones are included to ensure correct left or right insertions
                order.append(None)
                continue
            
            if node.left or node.right:
                bfs.append(node.left)
                bfs.append(node.right)
                
        return order
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for October 6th, 2020.
    '''
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        node = root
        while node:
            prev = node
            node = node.left if val < node.val else node.right
            
        if val < prev.val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
            
        return root
