 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthsmallest(self, root: TreeNode, k: int) -> int:
        '''
        Returns the kth smallest element from a binary search tree.
        
        Params:
            root - The root node of a binary search tree.
            
            k - Which number from the smallest to return. k = 1 returns
                the smallest.
                
        Returns:
            int - The kth smallest value in a given binary search tree.
            
        Example:
            Given the following bst:
                    3
                   / \
                  1   4
                   \
                    2
            kthsmallest(TreeNode(3), 1) returns 1
            
            
            Given the following bst:
                    5
                   / \
                  3   6
                 / \
                2   4
               /
              1
            kthsmallest(TreeNode(5), 3) returns 3
        '''
        if not root or k < 1:
            return 0
        
        dfs = []
        while k:
            while root:
                dfs.append(root)
                root = root.left
            
            if not dfs:
                return 0
            
            node = dfs.pop()
            k -= 1
            root = node.right
            
        return node.val
