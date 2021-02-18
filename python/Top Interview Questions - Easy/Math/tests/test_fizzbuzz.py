import unittest, sys
sys.path.append('..')
from fizzbuzz import Solution

class TestFizzBuzz(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_fizzBuzz(self):
        case_one = 1
        self.assertEqual(self.s.fizzBuzz(case_one), ['1'])
        
        case_two = 15
        self.assertEqual(self.s.fizzBuzz(case_two), ['1',
                                                     '2',
                                                     'Fizz',
                                                     '4',
                                                     'Buzz',
                                                     'Fizz',
                                                     '7',
                                                     '8',
                                                     'Fizz',
                                                     'Buzz',
                                                     '11',
                                                     'Fizz',
                                                     '13',
                                                     '14',
                                                     'FizzBuzz'])
        
if __name__ == '__main__':
    unittest.main()
