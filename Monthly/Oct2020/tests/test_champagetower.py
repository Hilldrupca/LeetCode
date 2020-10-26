import unittest, sys
sys.path.append('..')
from champagnetower import Solution

class TestChampagneTower(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_champagne_tower(self):
        case_one = {'poured': 1,
                    'query_row': 1,
                    'query_glass': 1}
        self.assertEqual(self.s.champagneTower(**case_one), 0)
        
        
        case_two = {'poured': 2,
                    'query_row': 1,
                    'query_glass': 1}
        self.assertEqual(self.s.champagneTower(**case_two), 0.5)
        
        
        case_three = {'poured': 100000009,
                      'query_row': 33,
                      'query_glass': 17}
        self.assertEqual(self.s.champagneTower(**case_three), 1.0)
        
if __name__ == '__main__':
    unittest.main()
