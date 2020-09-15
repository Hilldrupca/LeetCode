from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        Converts a sorted list to a binary search tree.
        
        Params:
            nums - A sorted list of integers.
            
        Returns:
            TreeNode - The root node of a binary search tree.
        '''
        if nums:
            return TreeNode(nums[len(nums)//2],
                            self.sortedArrayToBST(nums[:len(nums)//2]),
                            self.sortedArrayToBST(nums[len(nums)//2+1:]))
