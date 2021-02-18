import unittest, sys
sys.path.append('..')
from increasingordersearchtree import Solution, TreeNode

class TestIncreasingOrderSearchTree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_increasing_bst(self):
        '''
        CASE ONE:
        
                5
               / \
              3   6
             / \   \
            2   4   8
           /       / \
          1       7   9        
        '''
        case_one = TreeNode(5,
                            TreeNode(3,
                                     TreeNode(2,
                                              TreeNode(1)),
                                     TreeNode(4)),
                            TreeNode(6,
                                     None,
                                     TreeNode(8,
                                              TreeNode(7),
                                              TreeNode(9))))
                         
        self.assertEqual(self.s.increasingBST(case_one)._path(),
                         [1,2,3,4,5,6,7,8,9])
        
        '''
        CASE TWO:
        
            5
           / \
          1   7
        '''
        case_two = TreeNode(5,
                            TreeNode(1),
                            TreeNode(7))
        
        self.assertEqual(self.s.increasingBST(case_two)._path(),
                         [1,5,7])
        
if __name__ == '__main__':
    unittest.main()
