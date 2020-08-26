import unittest, sys
sys.path.append('..')
from fizzbuzz import Solution

class TestFizzBuzz(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().fizzbuzz
        
    def test_equals(self):
        case_one = 15
        exp_answer = ['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz',
                      'Buzz','11','Fizz','13','14','FizzBuzz']
        
        self.assertEqual(self.s(case_one), exp_answer)
        
if __name__ == '__main__':
    unittest.main()
