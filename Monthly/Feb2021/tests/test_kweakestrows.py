import unittest, sys
sys.path.append('..')
from kweakestrows import Solution

class TestKWeakestRows(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_k_weakest_rows(self):
        case_one = {'mat': [[1,1,0,0,0],
                              [1,1,1,1,0],
                              [1,0,0,0,0],
                              [1,1,0,0,0],
                              [1,1,1,1,1]],
                      'k': 3}
        
        self.assertEqual(self.s.kWeakestRows(**case_one), [2,0,3])
        
        case_two = {'mat': [[1,0,0,0],
                              [1,1,1,1],
                              [1,0,0,0],
                              [1,0,0,0]],
                      'k': 2}
        
        self.assertEqual(self.s.kWeakestRows(**case_two), [0,2])
        
if __name__ == '__main__':
    unittest.main()
