import unittest, sys
sys.path.append('..')
from missingnumber import Solution

class TestMissingNumber(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_missing_number(self):
        case_one = [3,0,1]
        self.assertEqual(self.s.missingNumber(case_one), 2)
        
        case_two = [9,6,4,2,3,5,7,0,1]
        self.assertEqual(self.s.missingNumber(case_two), 8)
        
        case_three = [3,2,1]
        self.assertEqual(self.s.missingNumber(case_three), 0)
        
if __name__ == '__main__':
    unittest.main()
