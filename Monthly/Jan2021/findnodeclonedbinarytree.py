
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 2nd, 2020.
    '''
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode,
                      target: TreeNode) -> TreeNode:
        '''
        Given a binary tree, it's clone, and a target node from the original
        tree, returns a reference to the same node in the cloned tree.
        
        Constraints:
            The number of nodes in the tree is in the range [1, 10**4]
            The values of the nodes of the tree are unique
            Target node is a node from the original tree and is not None.
            
        Params:
            original - The root node of the original binary tree.
            
            cloned - The root node of the cloned binary tree.
            
            target - The target node from the original binary tree.
            
        Returns;
            TreeNode - A reference to the target node found in the cloned
                       binary tree.
                       
        Example:
            **Assume target values are TreeNodes and not ints**
        
            Given the following original binary tree, a, and it's clone, ac:
            
                    7
                   / \
                  4   3 <- target
                     / \
                    6   19
                    
            getTargetCopy(a, ac, 3)   ->   TreeNode(3,
                                                    TreeNode(6),
                                                    TreeNode(19)) from ac
        '''
        if original is None:
            return
        
        if target == original:
            return cloned
        
        return self.getTargetCopy(original.left, cloned.left, target) or \
               self.getTargetCopy(original.right, cloned.right, target)
