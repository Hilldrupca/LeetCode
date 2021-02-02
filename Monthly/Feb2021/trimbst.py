from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def _inorder_traversal(self):
        '''Tester function. Returns the inorder traversal of a inary tree.'''
        res, stack = [], [self]
        
        while stack:
            node = stack.pop()
            
            if node is None:
                continue
            else:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return res
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for February 2nd, 2021.
    '''
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        '''
        Given the root of a binary search tree, the upper, and lower
        boundaries, trims the tree so tha all elements are between low and high.
        Returns the root node of the newly trimmed binary search tree.
        
        Constraints:
            The number of nodes in the tree is in the range [1, 10**4]
            0 <= node.val <= 10**4
            The value of each node in the tree is unique
            root is guaranteed to be a valid binary search tree
            0 <= low <= high <= 10**4
            
        Params:
            root - The root node of a binary search tree.
            
            low - An inclusive lower bound integer.
            
            high - An inclusive upper bound integer.
            
        Returns:
            TreeNode - The root node of the newly trimmed binary search tree.
            
        Examples:
            Input tree (left), and resulting tree (right):
            
                    1               1
                   / \      ->       \
                  0   2               2
                  
            Input tree (left), and resulting tree (right):
            
                    3
                   / \                3
                  0   4              /
                   \        ->      2
                    2              /
                   /              1
                  1
        '''
        def inorder_trim(node, q):
            if node is None:
                return
            
            if low <= node.val <= high:
                q.append(node.val)
                
            inorder_trim(node.left, q)
            inorder_trim(node.right,q)
            
        inorder = deque()
        inorder_trim(root, inorder)
        
        sentinel = node = TreeNode(val=inorder.popleft())
        stack = [(node, float('-inf'), float('inf'))]
        
        while inorder:
            
            while stack and (inorder[0] < stack[-1][1] or inorder[0] > stack[-1][2]):
                stack.pop()
               
            val = inorder.popleft()
            node, l, h = stack[-1]
            
            if node.val > val:
                node.left = TreeNode(val=val)
                stack.append((node.left, l, node.val))
            else:
                node.right = TreeNode(val=val)
                stack.append((node.right, node.val, h))
                
        return sentinel
