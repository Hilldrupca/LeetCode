import unittest, sys
sys.path.append('..')
from rangesumbst import Solution, TreeNode

class TestRangeSumBST(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_range_sum_bst(self):
        '''
        CASE ONE:
        low = 7
        high = 15
        
                10
               /  \
              5    15
             / \     \
            3   7     18
        '''
        case_one = TreeNode(10,
                            TreeNode(5,
                                     TreeNode(3),
                                     TreeNode(7)),
                            TreeNode(15,
                                     None,
                                     TreeNode(18)))
        self.assertEqual(self.s.rangeSumBST(case_one, 7, 15), 32)
        
        '''
        CASE TWO
        low = 6
        high = 10
                  __10__
                 /      \
                5        15
               / \      /  \
              3   7   13    18
             /   /
            1   6
        '''
        case_two = TreeNode(10,
                            TreeNode(5,
                                     TreeNode(3,
                                              TreeNode(1)),
                                     TreeNode(7,
                                              TreeNode(6))),
                            TreeNode(15,
                                     TreeNode(13),
                                     TreeNode(18)))
        self.assertEqual(self.s.rangeSumBST(case_two, 6, 10), 23)
        
        '''
        CASE THREE - none passed
        '''
        case_three = None
        self.assertEqual(self.s.rangeSumBST(case_three, float('-inf'),
                                            float('inf')), 0)
        
if __name__ == '__main__':
    unittest.main()
