import unittest, sys
sys.path.append('..')
from plusone import Solution

class TestPlusOne(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = [1,2,3]
        answer_one = self.s.plusone(case_one)
        self.assertEqual(answer_one, [1,2,4])
        
        case_two = [4,3,2,1]
        answer_two = self.s.plusone(case_two)
        self.assertEqual(answer_two, [4,3,2,2])
        
        case_three = [9,9]
        answer_three = self.s.plusone(case_three)
        self.assertEqual(answer_three, [1,0,0])
        
if __name__ == '__main__':
    unittest.main()
