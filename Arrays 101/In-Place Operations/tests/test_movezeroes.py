import unittest, sys
sys.path.append('..')
from movezeroes import Solution

class TestMoveZeroes(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_move_zeroes(self):
        nums = [0,1,0,3,12]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1,3,12,0,0])
        
if __name__ == '__main__':
    unittest.main()
