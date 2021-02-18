import unittest, sys
sys.path.append('..')
from numevendigits import Solution

class TestNumEvenDigits(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_numbers(self):
        case_one = [12,345,2,6,7896]
        self.assertEqual(self.s.findNumbers(case_one), 2)
        
        case_two = [555,901,482,1771]
        self.assertEqual(self.s.findNumbers(case_two), 1)
        
if __name__ == '__main__':
    unittest.main()
