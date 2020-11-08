import unittest, sys
sys.path.append('..')
from sortbyparity import Solution

class TestSortByParity(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_sort_array_by_parity(self):
        self.assertEqual(self.s.sortArrayByParity([3,1,2,4]), [4,2,1,3])
        
if __name__ == '__main__':
    unittest.main()
