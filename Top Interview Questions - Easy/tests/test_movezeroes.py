import unittest, sys
sys.path.append('..')
from movezeroes import Solution

class TestMoveZeroes(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = [0,1,0,3,12]
        self.s.moveZeroes(case_one)
        self.assertEqual(case_one, [1,3,12,0,0])
        
if __name__ == '__main__':
    unittest.main()
