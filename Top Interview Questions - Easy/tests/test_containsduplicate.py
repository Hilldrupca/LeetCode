import unittest, sys
sys.path.append('..')
from containsduplicate import Solution

class TestContainsDuplicate(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = [1,2,3,1]
        self.assertEqual(self.s.containsDuplicate(case_one), True)
        
        case_two = [1,2,3,4]
        self.assertEqual(self.s.containsDuplicate(case_two), False)
        
        case_three = [1,1,1,3,3,4,3,2,4,2]
        self.assertEqual(self.s.containsDuplicate(case_three), True)
        
if __name__ == '__main__':
    unittest.main()
