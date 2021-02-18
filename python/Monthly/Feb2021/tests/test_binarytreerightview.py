import unittest, sys
sys.path.append('..')
from binarytreerightview import Solution, TreeNode

class TestBinaryTreeRightView(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_right_side_view(self):
        '''
        CASE ONE
        
                1
               / \
              2   3
               \   \
                5   4
        '''
        case_one = TreeNode(1,
                            TreeNode(2,
                                     None,
                                     TreeNode(5)),
                            TreeNode(3,
                                     None,
                                     TreeNode(4)))
        
        self.assertEqual(self.s.rightSideView(case_one), [1,3,4])
        
        '''
        CASE TWO - empty tree
        '''
        case_two = None
        
        self.assertEqual(self.s.rightSideView(case_two), [])
        
if __name__ == '__main__':
    unittest.main()
