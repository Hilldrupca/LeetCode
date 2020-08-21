import unittest, sys
sys.path.append('..')
from rotatearray import Solution

class TestRotateArray(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = [1,2,3,4,5,6,7]
        self.s.rotate(case_one, 3)
        self.assertEqual(case_one, [5,6,7,1,2,3,4])
        
        case_two = [-1,-100,3,99]
        self.s.rotate(case_two, 2)
        self.assertEqual(case_two, [3,99,-1,-100])
        
if __name__ == '__main__':
    unittest.main()
