from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for September 8th, 2020.
    '''
    def sumRootToLeaf(self, root: TreeNode) -> int:
        '''
        Given a binary tree, each node has value 0 or 1.  Each root-to-leaf
        path represents a binary number starting with the most significant
        bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this
        could represent 01101 in binary, which is 13.

        For all leaves in the tree, consider the numbers represented by the
        path from the root to that leaf.
        
        Params:
            root - The beginning node of a binary tree.
            
        Returns:
            int - the sum of the leaf node binary paths.
            
        Example:
        
            Given the following binary tree:
                        1
                       / \
                      /   \
                     0     1
                    / \   / \
                   0   1 0   1
                   ^   ^ ^   ^
                   1   2 3   4
                   
            The paths to the leaf nodes labeled 1, 2, 3, 4 would be:
                100, 101, 110, 111
                
            These represent the decimal numbers 4, 5, 6, 7. Adding them
            results in 22. This value is what is returned.
        '''
        bfs = deque()
        bfs.append((root, root.val))
        
        total = 0
        while bfs:
            node, value = bfs.popleft()
            
            if node.left:
                bfs.append((node.left, value*2 + node.left.val))
            
            if node.right:
                bfs.append((node.right, value*2 + node.right.val))
                
            if not node.left and not node.right:
                total += value
                
        return total
