import unittest, sys
sys.path.append('..')
from sumleftleaves import Solution, TreeNode

class TestSumLeftLeaves(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        '''
        Case one:   3
                   / \
                  9  20
                    /  \
                   15   7
        '''
        case_one = TreeNode(3)
        case_one.left = TreeNode(9)
        case_one.right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
        
        answer_one = self.s.sumOfLeftLeaves(case_one)
        self.assertEqual(answer_one, 24)
        
        '''
        Case two:   1
                   /
                  2
        '''
        case_two = TreeNode(1, left=TreeNode(2))
        answer_two = self.s.sumOfLeftLeaves(case_two)
        self.assertEqual(answer_two, 2)
        
        '''
        Case three:     1    <- no left or right nodes
        '''
        case_three = TreeNode(1)
        answer_three = self.s.sumOfLeftLeaves(case_three)
        self.assertEqual(answer_three, 0)
        
        '''
        Case four:  []  <- empty list
        '''
        case_four = []
        answer_four = self.s.sumOfLeftLeaves(case_four)
        self.assertEqual(answer_four, 0)
        
if __name__ == '__main__':
    unittest.main()
