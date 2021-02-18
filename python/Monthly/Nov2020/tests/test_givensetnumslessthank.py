import unittest, sys
sys.path.append('..')
from givensetnumslessthank import Solution

class TestGivenSetNumsLessThanK(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().atMostNGivenDigitSet
        
    def test_at_most_n_given_digit_set(self):
        case_one = {'digits': ["1","3","5","7"],
                    'n': 100}
        self.assertEqual(self.s(**case_one), 20)
        
        case_two = {'digits': ["1","4","9"],
                    'n': 1000000000}
        self.assertEqual(self.s(**case_two), 29523)
        
        case_three = {'digits': ["1","2","3","4","6","7","8","9"],
                      'n': 1000000000}
        self.assertEqual(self.s(**case_three), 153391688)
        
        case_four = {'digits': ["1","2","3","4","6","7","8","9"],
                     'n': 67688637}
        self.assertEqual(self.s(**case_four), 12255070)
        
        case_five = {'digits': ["7"],
                     'n': 8}
        self.assertEqual(self.s(**case_five), 1)
        
        case_six = {'digits': ["3","5"],
                    'n': 4}
        self.assertEqual(self.s(**case_six), 1)
        
        case_seven = {'digits': ["5","6"],
                      'n': 19}
        self.assertEqual(self.s(**case_seven), 2)
        
        case_eight = {'digits': ["5","7","8"],
                      'n': 59}
        self.assertEqual(self.s(**case_eight), 6)
        
        # Empty digits passed
        self.assertEqual(self.s([], 10), 0)
        
        # No target number
        self.assertEqual(self.s(['1','2','3'], 0), 0)
        
if __name__ == '__main__':
    unittest.main()
