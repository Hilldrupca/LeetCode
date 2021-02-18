from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
    def next_node_path(self):
        res = []
        nodes = deque([self])
        while nodes:
            node = nodes.popleft()
            if node.next:
                res.append(node.next.val)
            else:
                res.append(None)
            
            if node.left:
                nodes.append(node.left)
                nodes.append(node.right)
                
        return res
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 13th, 2020.
    '''
    def connect(self, root: TreeNode) -> TreeNode:
        '''
        Given a perfect binary tree, populates each node's next pointer to the
        node on its right.
        
        A perfect binary tree has all leaf nodes on the same level, and every
        parent node has two children.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            TreeNode - The root node.
            
        Example:
            Given the following binary tree, b:
                          __1__
                         /     \
                        2       3
                       / \     / \
                      4   5   6   7
                       
            connect(b) modifies it to:
                          __1__
                         /     \
                        2   >   3
                       / \     / \
                      4 > 5 > 6 > 7
        '''
        if not root:
            return
        
        leftmost = root
        
        while leftmost.left:
            cur = leftmost
            
            while cur:
                cur.left.next = cur.right
                
                if cur.next:
                    cur.right.next = cur.next.left
                    
                cur = cur.next
                
            leftmost = leftmost.left
            
        return root
