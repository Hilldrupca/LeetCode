import unittest, sys
sys.path.append('..')
from peakelement import Solution

class TestPeakElement(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_peak_element(self):
        case_one = [1,2,3,1]
        self.assertEqual(self.s.findPeakElement(case_one), 2)
        
        
        case_two = [1,2,1,3,5,6,4]
        self.assertIn(self.s.findPeakElement(case_two), [1,5])
        
        
        case_three = [1,2]
        self.assertEqual(self.s.findPeakElement(case_three), 1)
        
        
        case_four = [2,1]
        self.assertEqual(self.s.findPeakElement(case_four), 0)
        
if __name__ == '__main__':
    unittest.main()
