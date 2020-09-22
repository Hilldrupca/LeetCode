import unittest, sys
sys.path.append('..')
from majorityelement2 import Solution

class TestMajorityElement2(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_majorityElement(self):
        case_one = [3,2,3]
        self.assertEqual(self.s.majorityElement(case_one), [3])
        
        case_two = [1,1,1,3,3,2,2,2]
        self.assertEqual(self.s.majorityElement(case_two), [1,2])
        
if __name__ == '__main__':
    unittest.main()
