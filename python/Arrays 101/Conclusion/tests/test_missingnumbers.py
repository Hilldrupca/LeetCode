import unittest, sys
sys.path.append('..')
from missingnumbers import Solution

class TestMissingNumbers(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_disappeared_numbers(self):
        case_one = [4,3,2,7,8,2,3,1]
        self.assertEqual(self.s.findDisappearedNumbers(case_one), [5,6])
        
        case_two = [1,2,1]
        self.assertEqual(self.s.findDisappearedNumbers(case_two), [3])
        
        case_three = []
        self.assertEqual(self.s.findDisappearedNumbers(case_three), [])
        
if __name__ == '__main__':
    unittest.main()
