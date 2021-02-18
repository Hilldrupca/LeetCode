import unittest, sys
sys.path.append('..')
from gasstation import Solution

class TestGasStation(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().canCompleteCircuit
        
    def test_circuit(self):
        case_one = {'gas': [1,2,3,4,5],
                    'cost': [3,4,5,1,2]}
        self.assertEqual(self.s(**case_one), 3)
        
        case_two = {'gas': [2,3,4],
                    'cost': [3,4,3]}
        self.assertEqual(self.s(**case_two), -1)
        
if __name__ == '__main__':
    unittest.main()
