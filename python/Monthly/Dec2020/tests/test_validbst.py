import unittest, sys
sys.path.append('..')
from validbst import Solution, TreeNode

class TestValidBST(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_is_valid_bst(self):
        '''
        CASE ONE
        
                2
               / \
              1   3
        '''
        case_one = TreeNode(2,
                            TreeNode(1),
                            TreeNode(3))
        
        self.assertTrue(self.s.isValidBST(case_one))
        
        '''
        CASE TWO
        
                5
               / \
              1   4
                 / \
                3   6
        '''
        case_two = TreeNode(5,
                            TreeNode(1),
                            TreeNode(4,
                                     TreeNode(3),
                                     TreeNode(6)))
        
        self.assertFalse(self.s.isValidBST(case_two))
        
        '''
        CASE THREE
        
                1
               /
              1
        '''
        case_three = TreeNode(1,
                              TreeNode(1))
        
        self.assertFalse(self.s.isValidBST(case_three))
        
        '''
        CASE FOUR - single node
        
                1
        '''
        case_four = TreeNode(1)
        
        self.assertTrue(self.s.isValidBST(case_four))
        
if __name__ == '__main__':
    unittest.main()
