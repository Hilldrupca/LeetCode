import unittest, sys
sys.path.append('..')
from mostcompetitivesubsequence import Solution

class TestMostCompetitiveSubsequence(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_most_competitive(self):
        case_one = {'nums': [3,5,2,6],
                    'k': 2}
        self.assertEqual(self.s.mostCompetitive(**case_one), [2,6])
        
        case_two = {'nums': [2,4,3,3,5,4,9,6],
                    'k': 4}
        self.assertEqual(self.s.mostCompetitive(**case_two), [2,3,3,4])
        
        case_three = {'nums': [11,52,57,91,47,95,86,46,87,47,70,56,54,61,
                               89,44,3,73,1,7,87,48,17,25,49,54,6,72,97,62,
                               16,11,47,34,68,58,14,36,46,65,2,15],
                      'k': 18}
        self.assertEqual(self.s.mostCompetitive(**case_three),
                         [1,7,6,72,97,62,16,11,47,34,68,58,14,36,46,65,2,15])
        
if __name__ == '__main__':
    unittest.main()
