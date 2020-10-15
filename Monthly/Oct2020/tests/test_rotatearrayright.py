import unittest, sys
sys.path.append('..')
from rotatearrayright import Solution

class TestRotateArrayRight(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_rotate(self):
        case_one = {'nums': [1,2,3,4,5,6,7],
                    'k': 3}
        
        self.s.rotate(**case_one)
        self.assertEqual(case_one['nums'], [5,6,7,1,2,3,4])
        
        
        case_two = {'nums': [-1,-100,3,99],
                    'k': 2}
        
        self.s.rotate(**case_two)
        self.assertEqual(case_two['nums'], [3,99,-1,-100])
        
if __name__ == '__main__':
    unittest.main()
