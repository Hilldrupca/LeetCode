import unittest, sys
sys.path.append('..')
from shortestdistancetochar import Solution

class TestShortestDistanceToChar(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_shortest_to_char(self):
        case_one = {'s': 'loveleetcode',
                    'c': 'e'}
        
        self.assertEqual(self.s.shortestToChar(**case_one),
                         [3,2,1,0,1,0,0,1,2,2,1,0])
        
        case_two = {'s': 'aaab',
                    'c': 'b'}
        
        self.assertEqual(self.s.shortestToChar(**case_two), [3,2,1,0])
        
        case_three = {'s': 'aaba',
                      'c': 'b'}
        
        self.assertEqual(self.s.shortestToChar(**case_three), [2,1,0,1])
        
if __name__ == '__main__':
    unittest.main()
