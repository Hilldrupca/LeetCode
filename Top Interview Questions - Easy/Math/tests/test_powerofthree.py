import unittest, sys
sys.path.append('..')
from powerofthree import Solution

class TestPowerOfThree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_power_of_three(self):
        case_true = [27, 9, 243]
        for x in case_true:
            self.assertTrue(self.s.isPowerOfThree(x))
            
        case_false = [0, 45, 8]
        for x in case_false:
            self.assertFalse(self.s.isPowerOfThree(x))
            
if __name__ == '__main__':
    unittest.main()
