import unittest, sys
sys.path.append('..')
from nextpermutation import Solution

class TestNextPermuation(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_next_permuation(self):
        case_one = [1,2,3]
        self.s.nextPermutation(case_one)
        self.assertEqual(case_one, [1,3,2])
        
        case_two = [3,2,1]
        self.s.nextPermutation(case_two)
        self.assertEqual(case_two, [1,2,3])
        
        case_three = [1,1,5]
        self.s.nextPermutation(case_three)
        self.assertEqual(case_three, [1,5,1])
        
        case_four = [1]
        self.s.nextPermutation(case_four)
        self.assertEqual(case_four, [1])
        
        case_five = [1,3,2]
        self.s.nextPermutation(case_five)
        self.assertEqual(case_five, [2,1,3])
        
        case_six = [1,3,2,4]
        self.s.nextPermutation(case_six)
        self.assertEqual(case_six, [1,3,4,2])
        
        case_seven = [2,3,1]
        self.s.nextPermutation(case_seven)
        self.assertEqual(case_seven, [3,1,2])
        
        case_eight = [1,5,1]
        self.s.nextPermutation(case_eight)
        self.assertEqual(case_eight, [5,1,1])
        
        case_nine = [5,4,7,5,3,2]
        self.s.nextPermutation(case_nine)
        self.assertEqual(case_nine, [5,5,2,3,4,7])
        
if __name__ == '__main__':
    unittest.main()
