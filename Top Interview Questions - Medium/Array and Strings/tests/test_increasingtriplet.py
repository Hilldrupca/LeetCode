import unittest, sys
sys.path.append('..')
from increasingtriplet import Solution

class TestIncreasingTriplet(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_increasing_triplet(self):
        cases = {'one': [1,2,3,4,5],
                 'two': [2,1,5,0,4,6],
                 'three': [5,4,3,2,1],
                 'four': [1,1,1,1,1],
                 'five': [1,2,2,1],
                 'six': [2,1,3]}
        
        self.assertTrue(self.s.increasingTriplet(cases['one']))
        self.assertTrue(self.s.increasingTriplet(cases['two']))
        
        self.assertFalse(self.s.increasingTriplet(cases['three']))
        self.assertFalse(self.s.increasingTriplet(cases['four']))
        self.assertFalse(self.s.increasingTriplet(cases['five']))
        self.assertFalse(self.s.increasingTriplet(cases['six']))
        
if __name__ == '__main__':
    unittest.main()
