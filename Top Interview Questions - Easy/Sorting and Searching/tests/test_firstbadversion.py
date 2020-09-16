from random import randint
import unittest, sys
sys.path.append('..')
from firstbadversion import Solution

class TestFirstBadVersion(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_bad_version(self):
        
        # Check within small number of versions
        self.s.first_bad_version = 4
        self.assertEqual(self.s.firstBadVersion(5), 4)
        
        # Check within large number of versions
        ver = randint(0,1000000)
        self.s.first_bad_version = ver
        self.assertEqual(self.s.firstBadVersion(1000000), ver)
        
        # Check version greater than upper bound
        self.s.first_bad_version = 10
        self.assertEqual(self.s.firstBadVersion(9), -1)

        # Check version less than lower bound
        self.s.first_bad_version = -2
        self.assertEqual(self.s.firstBadVersion(5), -1)
        
if __name__ == '__main__':
    unittest.main()
