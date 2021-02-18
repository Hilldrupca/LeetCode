from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        Determines if a binary tree is valid. Checks the order of node values,
        and if there are any duplicates.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            bool - Whether or not a binary tree is valid.
            
        Examples:
            Given the following binary tree:
                2
               / \
              1   3
            
            isValidBST()   ->   True
            
            Given the following binary Tree:
                    5
                   / \
                  1   4
                     / \
                    3   6
            
            isValidBST()   ->   False
        '''
        if not root:
            return True
        
        order = []
        self._subtree(root, order)
        
        right_order = order == sorted(order)
        no_dup = len(set(order)) == len(order)
        
        return right_order & no_dup
    
    def _subtree(self, node: TreeNode, order: List[int]) -> None:
        if node.left:
            self._subtree(node.left, order)
            
        order.append(node.val)
            
        if node.right:
            self._subtree(node.right, order)
