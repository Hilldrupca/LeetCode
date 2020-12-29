
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for December 29th, 2020.
    '''
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        '''
        Given a binary tree where node values are digits from 1 to 9, returns
        how many pseudo-palindromic paths exist within the tree. A
        pseudo-palindromic path is a path from root to leaf node whose nodes
        could be rearranged to make a palindrome.
        
        Constraints:
            Nodes in tree in the range [1, 10**5]
            1 <= node.val <= 9
            
        Params;
            root - The root node of a bianry tree.
        
        Returns:
            int - The number of pseudo-palindromic paths in the tree.
            
        Examples:
            Given the following tree, a:
            
                    2
                   / \
                  3   1
                 / \   \
                3   1   1
                
            pseudoPalindromicPaths(a)   ->   2, the paths [2,3,3], and [2,1,1]
                                             can be rearranged to palindromes.
                
            Given the following tree, b:
            
                    2
                   / \
                  1   1
                 / \
                1   3
                     \
                      1
                      
            pseudoPalindromicPaths(b)   ->   1, only the path [2,1,1] can be
                                             rearranged to a palindrome.
        '''
        node_val_counts = {x:0 for x in range(1,10)}
        palindrome_paths = 0
        
        def dfs(node, counts):
            if not node:
                return
            
            counts[node.val] += 1 # add current node.val to path
            
            # Check if path is pseudo-palindromic
            # Even length paths cannot contain digits appearing and odd number
            # of times
            # Odd length paths can only contain one digit that appears an odd
            # number of times
            if not node.left and not node.right:
                odd = total = 0
                for c in counts.values():
                    odd += c % 2
                    total += c
                
                nonlocal palindrome_paths
                if odd == total % 2:
                    palindrome_paths += 1

            else:
                dfs(node.left, counts) # explore left subtree
                dfs(node.right, counts) # explore right subtree
            
            counts[node.val] -= 1 # remove current node.val from path
            
        dfs(root, node_val_counts)
        return palindrome_paths
