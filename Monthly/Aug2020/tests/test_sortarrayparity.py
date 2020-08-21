import unittest,sys
sys.path.append('..')
from sortarrayparity import Solution

class TestSortArrayParity(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case = [3,1,2,4]
        possible = [[2,4,1,3], [2,4,3,1], [4,2,1,3], [4,2,3,1]]
        self.assertIn(self.s.sortArrayByParity(case), possible)
        
if __name__ == '__main__':
    unittest.main()
