from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 29th, 2021.
    '''
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        '''
        Returns the vertical order traversal node values of a binary tree.
        Nodes are sorted, and group by x coordinate. Within those groups node's
        are sorted by y coordinate then node value in case of conflicts. The
        root node is position (0,0). For each node at position (x, y) the left
        child is (x - 1, y - 1), and the right childe is (x + 1, y - 1).
        
        Constraints:
            Number of nodes in tree is in the range [1, 1000]
            0 <= node.val <= 1000
            
        Params:
            root - The root node of a binary tree.
            
        Returns:
            List[List[int]] - The binary tree's node values group and sorted by
                              vertical order traversal.
                              
        Examples:
            Given the following binary tree, a:
            
                    3
                   / \
                  9   20
                     /  \
                    15   7
                    
            verticalTraversal(a)   ->   [[9], [3,15], [20], [7]]
            
            Given the following binary tree, b:
            
                     1
                   /   \
                  2     3
                 / \   / \
                4   5 6   7
                
            verticalTraversal(b)   ->   [[4], [2], [1,5,6], [3], [7]]
        '''
        def dfs(x, y, node, coords):
            if node is None:
                return
            
            if x not in coords:
                coords[x] = {}
                
            if y not in coords[x]:
                coords[x][y] = []
                
            coords[x][y].append(node.val)
            
            dfs(x-1, y-1, node.left, coords)
            dfs(x+1, y-1, node.right, coords)
            
        coords = {}
        dfs(0, 0, root, coords)
        
        res = []
        for x in sorted(coords.keys()):
            res.append([])
            
            for y in sorted(coords[x].keys(), reverse=True):
                res[-1].extend(sorted(coords[x][y]))
                
        return res
