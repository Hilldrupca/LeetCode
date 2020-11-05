import unittest, sys
sys.path.append('..')
from removeelement import Solution
from collections import Counter

class TestRemoveElement(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_remove_element(self):
        case_one = {'nums': [3,2,2,3],
                    'val': 3}
        case_one_len = self.s.removeElement(**case_one)
        
        self.assertEqual(case_one_len, 2)
        self.assertEqual(Counter(case_one['nums']), Counter([2,2]))
        
        
        case_two = {'nums': [0,1,2,2,3,0,4,2],
                    'val': 2}
        case_two_len = self.s.removeElement(**case_two)
        
        self.assertEqual(case_two_len, 5)
        self.assertEqual(Counter(case_two['nums']), Counter([0,1,0,4,3]))

if __name__ == '__main__':
    unittest.main()
