import unittest, sys
sys.path.append('..')
from maxdiffnodeancestor import Solution, TreeNode

class TestMaxDiffNodeAncestor(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_max_ancestor_diff(self):
        '''
        CASE ONE

             8
            / \
           3   10
          / \    \
         1   6    14
            / \   /
           4   7 13
        '''
        case_one = TreeNode(8,
                            TreeNode(3,
                                     TreeNode(1),
                                     TreeNode(6,
                                              TreeNode(4),
                                              TreeNode(7))),
                            TreeNode(10,
                                     None,
                                     TreeNode(14,
                                              TreeNode(13))))
        self.assertEqual(self.s.maxAncestorDiff(case_one), 7)
        
        '''
        CASE TWO
            1
             \
              2
               \
                0
               /
              3
        '''
        case_two = TreeNode(1,
                            None,
                            TreeNode(2,
                                     None,
                                     TreeNode(0,
                                              TreeNode(3))))
        self.assertEqual(self.s.maxAncestorDiff(case_two), 3)
        
        '''
        CASE THREE
                    8
                     \
                      1__
                     /   \
                    5     6
                   / \   /
                  2   4  0
                 / \
                7   3
        '''
        case_three = TreeNode(8,
                              None,
                              TreeNode(1,
                                       TreeNode(5,
                                                TreeNode(2,
                                                         TreeNode(7),
                                                         TreeNode(3)),
                                                TreeNode(4)),
                                       TreeNode(6,
                                                TreeNode(0))))
        self.assertEqual(self.s.maxAncestorDiff(case_three), 8)
        
if __name__ == '__main__':
    unittest.main()
