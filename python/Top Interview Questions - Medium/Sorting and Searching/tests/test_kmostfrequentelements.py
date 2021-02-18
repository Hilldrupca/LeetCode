import unittest, sys
sys.path.append('..')
from kmostfrequentelements import Solution

class TestKMostFrequentElements(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_top_k_frequent(self):
        case_one = [1,1,1,2,2,3]
        self.assertEqual(self.s.topKFrequent(case_one, 2), [1,2])
        
        case_two = [1]
        self.assertEqual(self.s.topKFrequent(case_two, 1), [1])
        
if __name__ == '__main__':
    unittest.main()
