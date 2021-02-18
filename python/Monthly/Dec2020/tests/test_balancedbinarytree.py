import unittest, sys
sys.path.append('..')
from balancedbinarytree import Solution, TreeNode

class TestBalancedBinaryTree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_is_balanced(self):
        '''
        CASE ONE
        
                3
               / \
              9   20
                 /  \
                15   7
        '''
        case_one = TreeNode(3,
                            TreeNode(9),
                            TreeNode(20,
                                     TreeNode(15),
                                     TreeNode(7)))
        
        self.assertTrue(self.s.isBalanced(case_one))
        
        '''
        CASE TWO
        
                1
               / \
              2   2
             / \
            3   3
           / \
          4   4
        '''
        case_two = TreeNode(1,
                            TreeNode(2,
                                     TreeNode(3,
                                              TreeNode(4),
                                              TreeNode(4)),
                                     TreeNode(3)),
                            TreeNode(2))
        
        self.assertFalse(self.s.isBalanced(case_two))
        
        '''
        CASE THREE
        
                1
               / \
              2   2
             /     \
            3       3
           /         \
          4           4
        '''
        case_three = TreeNode(1,
                              TreeNode(2,
                                       TreeNode(3,
                                                TreeNode(4))),
                              TreeNode(2,
                                       None,
                                       TreeNode(3,
                                                None,
                                                TreeNode(4))))
                                       
        self.assertFalse(self.s.isBalanced(case_three))
        
        '''
        CASE FOUR - Single node
        
                1
        '''
        case_four = TreeNode(1)
        
        self.assertTrue(self.s.isBalanced(case_four))
        
        '''
        CASE FIVE - Empty Tree
        '''
        case_five = []
        self.assertTrue(self.s.isBalanced(case_five))
        
if __name__ == '__main__':
    unittest.main()
