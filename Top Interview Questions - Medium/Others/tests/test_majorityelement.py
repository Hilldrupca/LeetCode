import unittest, sys
sys.path.append('..')
from majorityelement import Solution

class TestMajorityElement(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_majority_element(self):
        self.assertEqual(self.s.majorityElement([3,2,3]), 3)
        self.assertEqual(self.s.majorityElement([2,2,1,1,1,2,2]), 2)
        
if __name__ == '__main__':
    unittest.main()
