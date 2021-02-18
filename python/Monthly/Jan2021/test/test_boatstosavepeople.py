import unittest, sys
sys.path.append('..')
from boatstosavepeople import Solution

class TestBoatsToSavePeople(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_num_rescue_boats(self):
        case_one = {'people': [1,2],
                    'limit': 3}
        self.assertEqual(self.s.numRescueBoats(**case_one), 1)
        
        case_two = {'people': [3,2,2,1],
                    'limit': 3}
        self.assertEqual(self.s.numRescueBoats(**case_two), 3)
        
        case_three = {'people': [3,5,3,4],
                      'limit': 4}
        self.assertEqual(self.s.numRescueBoats(**case_three), 4)
        
        case_four = {'people': [3,2,3,2,2],
                     'limit': 6}
        self.assertEqual(self.s.numRescueBoats(**case_four), 3)
        
if __name__ == '__main__':
    unittest.main()
