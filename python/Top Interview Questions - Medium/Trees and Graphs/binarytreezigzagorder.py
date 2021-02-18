from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        Returns the zigzag level order traversal of a binary tree.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            List[List[int]] - A list of lists where each inner list is the
                              order of nodes for that level. Level order
                              alternates betwen left-right and right-left.
                              
        Example:
            Given the following binary tree:
                    3
                   / \
                  9   20
                     /  \
                    15   7
            
            zigzagOrderTraversal() returns [[3],[20,9],[15,7]]
        '''
        if not root:
            return []
        
        zigzag = [[]]
        level = deque()
        
        direction = 1   # 1 for right, 0 for left
        
        bfs = deque()
        bfs.append(root)
        while bfs:
            node = bfs.popleft()
            
            if node:
                zigzag[-1].append(node.val)
            
                if direction:
                    level.appendleft(node.left)
                    level.appendleft(node.right)
                else:
                    level.appendleft(node.right)
                    level.appendleft(node.left)
            
            if not bfs and level:
                direction = 0 if direction else 1
                bfs.extend(level)
                level = deque()
                zigzag.append([])
                
        if not zigzag[-1]:
            zigzag.pop(-1)
        
        return zigzag
