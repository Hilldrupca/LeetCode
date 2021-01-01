import unittest, sys
sys.path.append('..')
from checkarrayconcatenation import Solution

class TestCheckArrayConcatenation(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_can_form_array(self):
        case_one = {'arr': [85],
                    'pieces': [[85]]}
        self.assertTrue(self.s.canFormArray(**case_one))
        
        case_two = {'arr': [85,1,2],
                    'pieces': [[85,2,1]]}
        self.assertFalse(self.s.canFormArray(**case_two))
        
        case_three = {'arr': [15,88],
                      'pieces': [[88],[15]]}
        self.assertTrue(self.s.canFormArray(**case_three))
        
        case_four = {'arr': [49,18,16],
                     'pieces': [[16,18,49]]}
        self.assertFalse(self.s.canFormArray(**case_four))
        
        case_five = {'arr': [91,4,64,78],
                     'pieces': [[78],[4,64],[91]]}
        self.assertTrue(self.s.canFormArray(**case_five))
        
if __name__ == '__main__':
    unittest.main()
