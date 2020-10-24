import unittest, sys
sys.path.append('..')
from bagoftokens import Solution

class TestBagOfTokens(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_bag_of_tokens_score(self):
        case_one = {'tokens': [100],
                    'P': 50}
        self.assertEqual(self.s.bagOfTokensScore(**case_one), 0)
        
        
        case_two = {'tokens': [100,200],
                    'P': 150}
        self.assertEqual(self.s.bagOfTokensScore(**case_two), 1)
        
        
        case_three = {'tokens': [100,200,300,400],
                      'P': 200}
        self.assertEqual(self.s.bagOfTokensScore(**case_three), 2)
        
        
        case_four = {'tokens': [81,91,31],
                     'P': 73}
        self.assertEqual(self.s.bagOfTokensScore(**case_four), 1)
        
        
        case_five = {'tokens': [71,55,82],
                     'P': 54}
        self.assertEqual(self.s.bagOfTokensScore(**case_five), 0)
        
if __name__ == '__main__':
    unittest.main()
