import unittest, sys
sys.path.append('..')
from threesumclosest import Solution

class TestThreeSumClosest(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_three_sum_closest(self):
        # Trying out TestCase.subTest
        case_one = {'nums': [-1,2,1,-4],
                    'target': 2}
        with self.subTest(**case_one):
            self.assertEqual(self.s.threeSumClosest(**case_one), 2)
            
        case_two = {'nums': [0,1,1,2],
                    'target': 2}
        with self.subTest(**case_two):
            self.assertEqual(self.s.threeSumClosest(**case_two), 2)
            
        case_three = {'nums': [1,2],
                      'target': 2}
        with self.subTest('List must be at least len 3',**case_three):
            self.assertRaises(ValueError,
                              self.s.threeSumClosest,
                              **case_three)
            
if __name__ == '__main__':
    unittest.main()
