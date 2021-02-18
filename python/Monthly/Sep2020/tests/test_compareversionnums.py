import unittest, sys
sys.path.append('..')
from compareversionnums import Solution

class TestCompareVersionNums(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_comparison(self):
        case_one = ['0.1', '1.1']
        self.assertEqual(self.s.compareVersion(*case_one), -1)
        
        case_two = ['1.0.1', '1']
        self.assertEqual(self.s.compareVersion(*case_two), 1)
        
        case_three = ['7.5.2.4', '7.5.3']
        self.assertEqual(self.s.compareVersion(*case_three), -1)
        
        case_four = ['1.01', '1.001']
        self.assertEqual(self.s.compareVersion(*case_four), 0)
        
        case_five = ['1.0', '1.0.0']
        self.assertEqual(self.s.compareVersion(*case_five), 0)
        
        case_six = ['01', '1']
        self.assertEqual(self.s.compareVersion(*case_six), 0)
        
if __name__ == '__main__':
    unittest.main()
