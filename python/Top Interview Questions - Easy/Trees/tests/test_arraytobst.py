import unittest, sys
sys.path.append('..')
from arraytobst import Solution
import validbst

class TestArrayToBST(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        self.validbst = validbst.Solution().isValidBST
        
    def test_converted_bst(self):
        case_one = [-10,-3,0,5,9]
        case_one_ans = self.s.sortedArrayToBST(case_one)
        self.assertTrue(self.validbst(case_one_ans))
        
        case_two = [0,1,2,3,4,5]
        case_two_ans = self.s.sortedArrayToBST(case_two)
        self.assertTrue(self.validbst(case_two_ans))
        
        case_three = []
        self.assertEqual(self.s.sortedArrayToBST(case_three), None)
        
if __name__ == '__main__':
    unittest.main()
