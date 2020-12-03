
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def _path(self):
        '''
        Used for testing correct order of increasing order search tree.
        '''
        res, node = [], self
        
        while node:
            res.append(node.val)
            node = node.right
            
        return res
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for December 3rd, 2020.
    '''
    def increasingBST(self, root: TreeNode) -> TreeNode:
        '''
        Given the root of a binary search tree, rearranges the tree in-order so
        that the leftmost node in the tree becomes the root, and every node no
        longer has a left child.
        
        Params:
            root - The root node of a binary search tree.
            
        Returns:
            TreeNode - The new root node after rearranging tree.
            
        Example:
            Given the following binary search tree, a:
            
                        5
                       / \
                      3   6
                     / \   \
                    2   4   8
                   /       / \
                  1       7   9
                  
             After increasingBST(a), a becomes:
             
                1
                 \
                  2
                   \
                    3
                     \
                      ...
                       \
                        9
        '''
        sent_root = sent = TreeNode()
        
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            nonlocal sent
            root.left, sent.right = None, root
            sent = sent.right
            helper(root.right)
            
        helper(root)
        
        return sent_root.right
