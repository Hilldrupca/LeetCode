import unittest, sys
sys.path.append('..')
from singlenumber import Solution

class TestSingleNumber(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = [2,2,1]
        answer_one = self.s.singleNumber(case_one)
        self.assertEqual(answer_one, 1)
        
        case_two = [4,1,2,1,2]
        answer_two = self.s.singleNumber(case_two)
        self.assertEqual(answer_two, 4)
        
if __name__ == '__main__':
    unittest.main()
