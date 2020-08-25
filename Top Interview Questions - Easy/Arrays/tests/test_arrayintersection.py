import unittest, sys
sys.path.append('..')
from arrayintersection import Solution
from collections import Counter

class TestArrayIntersection(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        '''
        Yes, I realize my implementation in arrayintersection.py
        essentially uses collections.Couner. I learned about them
        afterwards.
        '''
        
        case_one = [[1,2,2,1], [2,2]]
        answer_one = self.s.intersect(*case_one)
        self.assertEqual(Counter(answer_one), Counter([2,2]))
        
        case_two = [[4,9,5], [9,4,9,8,4]]
        answer_two = self.s.intersect(*case_two)
        self.assertEqual(Counter(answer_two), Counter([4,9]))
        
if __name__ == '__main__':
    unittest.main()
