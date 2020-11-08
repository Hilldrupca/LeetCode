from typing import List
from collections import deque

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
        
class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        '''
        Returns the level order traversal of an n-ary tree.
        
        Params:
            root - The root node of an n-ary tree.
            
        Returns:
            List[List[int]] - A list of lists where each inner list is the
                              nodes for that level from left to right.
                              
        Examples:
            Given the following n-ary tree, a:
                    1
                   /|\
                  3 2 4
                 / \
                5   6
                
            levelOrder(a)   ->   [[1],[3,2,4],[5,6]]
            
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
                  
            levelOrder(b)   ->   [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
        '''
        if root is None:
            return []
        
        order = []
        bfs = deque([[root]])
        while bfs:
            level = bfs.popleft()
            next_level = []
            order.append([])
            for node in level:
                order[-1].append(node.val)
                next_level.extend(node.children)
                
            if next_level:
                bfs.append(next_level)
            
        return order
