import unittest, sys
sys.path.append('..')
from consecutivedifference import Solution

class TestConsecutiveDifference(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
    
    def test_equals(self):
        self.assertEqual(self.s.numsSameConsecDiff(3,7), [181,292,707,818,929])
        
        self.assertEqual(self.s.numsSameConsecDiff(2,1),
                         [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98])

if __name__ == '__main__':
    unittest.main()
