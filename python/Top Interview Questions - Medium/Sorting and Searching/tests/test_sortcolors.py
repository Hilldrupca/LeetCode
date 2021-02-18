import unittest, sys
sys.path.append('..')
from sortcolors import Solution

class TestSortColors(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_sort_colors(self):
        case_one = [2,0,2,1,1,0]
        self.s.sortColors(case_one)
        self.assertEqual(case_one, [0,0,1,1,2,2])
        
        
        case_two = [2,0,1]
        self.s.sortColors(case_two)
        self.assertEqual(case_two, [0,1,2])
        
        
        case_three = []
        self.s.sortColors(case_three)
        self.assertEqual(case_three, [])
        
if __name__ == '__main__':
    unittest.main()
