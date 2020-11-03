import unittest, sys
sys.path.append('..')
from duplicatezeroes import Solution

class TestDuplicateZeroes(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_duplicate_zeroes(self):
        case_one = [1,0,2,3,0,4,5,0]
        self.s.duplicateZeroes(case_one)
        self.assertEqual(case_one, [1,0,0,2,3,0,0,4])
        
        
        case_two = [1,2,3]
        self.s.duplicateZeroes(case_two)
        self.assertEqual(case_two, [1,2,3])
        
        
        case_three = [0,0,0]
        self.s.duplicateZeroes(case_three)
        self.assertEqual(case_three, [0,0,0])
        
        
        case_four = []
        self.s.duplicateZeroes(case_four)
        self.assertEqual(case_four, [])
        
if __name__ == '__main__':
    unittest.main()
