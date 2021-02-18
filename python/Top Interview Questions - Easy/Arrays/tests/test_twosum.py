import unittest, sys
sys.path.append('..')
from twosum import Solution

class TestTwoSum(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = {'nums': [2,7,11,15], 'target': 9}
        answer_one = self.s.twoSum(**case_one)
        self.assertEqual(answer_one, [0,1])
                         
if __name__ == '__main__':
    unittest.main()
