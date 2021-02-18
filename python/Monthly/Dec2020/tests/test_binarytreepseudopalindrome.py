import unittest, sys
sys.path.append('..')
from binarytreepseudopalindrome import Solution, TreeNode

class TestBinaryTreePseudoPalindrome(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().pseudoPalindromicPaths
        
    def test_pseudo_palindromic_paths(self):
        '''
        CASE ONE
        
                2
               / \
              3   1
             / \   \
            3   1   1
        '''
        case_one = TreeNode(2,
                            TreeNode(3,
                                     TreeNode(3),
                                     TreeNode(1)),
                            TreeNode(1,
                                     None,
                                     TreeNode(1)))
        
        self.assertEqual(self.s(case_one), 2)
        
        '''
        CASE TWO
        
                2
               / \
              1   1
             / \
            1   3
                 \
                  1
        '''
        case_two = TreeNode(2,
                            TreeNode(1,
                                     TreeNode(1),
                                     TreeNode(3,
                                              None,
                                              TreeNode(1))),
                            TreeNode(1))
                                     
        self.assertEqual(self.s(case_two), 1)
        
        '''
        CASE Three - single node
        
                3
        '''
        case_three = TreeNode(3)
        
        self.assertEqual(self.s(case_three), 1)
        
        '''
        CASE FOUR - empty tree
        '''
        case_four = None
        
        self.assertEqual(self.s(case_four), 0)
        
if __name__ == '__main__':
    unittest.main()
