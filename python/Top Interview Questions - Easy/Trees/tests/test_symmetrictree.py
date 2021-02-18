import unittest, sys
sys.path.append('..')
from symmetrictree import Solution, TreeNode

class TestSymmetricTree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_symmetry(self):
        '''
                1
               / \
              /   \
             2     2
            / \   / \
           3   4 4   3
        '''
        case_one = TreeNode(1,
                            left=TreeNode(2,
                                          left=TreeNode(3),
                                          right=TreeNode(4)),
                            right=TreeNode(2,
                                           left=TreeNode(4),
                                           right=TreeNode(3)))
        self.assertTrue(self.s.isSymmetric(case_one))
        
        '''
                1
               / \
              2   2
               \   \
                3   3
        '''
        case_two = TreeNode(1,
                            left=TreeNode(2,
                                          right=TreeNode(3)),
                            right=TreeNode(2,
                                           right=TreeNode(3)))
        self.assertFalse(self.s.isSymmetric(case_two))
        
if __name__ == '__main__':
    unittest.main()
