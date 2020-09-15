from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        bfs = deque()
        bfs.append([root])
        
        while bfs:
            level = bfs.popleft()
            
            res.append([])
            next_level = []
            for node in level:
                res[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            if next_level:
                bfs.append(next_level)
                
        return res
