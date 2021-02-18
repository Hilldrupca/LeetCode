import unittest, sys
sys.path.append('..')
from longestmountain import Solution

class TestLongestMountain(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_longest_mountain(self):
        case_one = [2,1,4,7,3,2,5]
        self.assertEqual(self.s.longestMountain(case_one), 5)
        
        case_two = [2,2,2]
        self.assertEqual(self.s.longestMountain(case_two), 0)
        
        case_three = [3,2,1]
        self.assertEqual(self.s.longestMountain(case_three), 0)
        
        case_four = [1,2,3]
        self.assertEqual(self.s.longestMountain(case_four), 0)
        
        case_five = [1,2,1]
        self.assertEqual(self.s.longestMountain(case_five), 3)
        
        case_six = [2,3,3,2,0,2]
        self.assertEqual(self.s.longestMountain(case_six), 0)
        
        case_seven = [0,0,1,0,0,1,1,1,1,1]
        self.assertEqual(self.s.longestMountain(case_seven), 3)
        
if __name__ == '__main__':
    unittest.main()
