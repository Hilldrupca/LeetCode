from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Returns the node values in inorder traversal order.
        
        
        Examples:
                1   <-  root
                 \
                  2
                 /
                3
            inorderTraversal() on the above returns [1,3,2]
            
            
                1   <-  root
               /
              2
              
            inorderTraversal() on the above returns [2,1]
            
            
                1   <-  root
                 \
                  2
                  
            inorderTraveral() on the above returns [1,2]
        '''
        if not root:
            return []
        
        order = []
        
        dfs = [(root,0)]
        while dfs:
            node, seen = dfs.pop(-1)
            
            if seen:
                order.append(node.val)
                continue
                
            if node.right:
                dfs.append((node.right,0))
                
            dfs.append((node,1))
            
            if node.left:
                dfs.append((node.left,0))
                
        return order
