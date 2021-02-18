import unittest, sys
sys.path.append('..')
from largestnumber import Solution

class TestLargestNumber(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_largest_number(self):
        self.assertEqual(self.s.largestNumber([10,2]), '210')
        self.assertEqual(self.s.largestNumber([3,30,34,5,9]), '9534330')
        self.assertEqual(self.s.largestNumber([10,2,1]), '2110')
        self.assertEqual(self.s.largestNumber([1,20]), '201')
        self.assertEqual(self.s.largestNumber([123,321]), '321123')
        self.assertEqual(self.s.largestNumber([1,1,1]), '111')
        self.assertEqual(self.s.largestNumber([121,12]), '12121')
        self.assertEqual(self.s.largestNumber([830,8308]), '8308830')
        self.assertEqual(self.s.largestNumber([824,8247]), '8248247')
        
if __name__ == '__main__':
    unittest.main()
