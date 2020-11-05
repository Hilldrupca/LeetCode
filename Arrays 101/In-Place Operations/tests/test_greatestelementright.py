import unittest, sys
sys.path.append('..')
from greatestelementright import Solution

class TestGreatestElementRight(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_replaceElements(self):
        case_one = [17,18,5,4,6,1]
        self.s.replaceElements(case_one)
        self.assertEqual(case_one, [18,6,6,6,1,-1])
        
        case_two = [1]
        self.s.replaceElements(case_two)
        self.assertEqual(case_two, [-1])
        
        case_three = []
        self.s.replaceElements(case_three)
        self.assertEqual(case_three, [])
        
if __name__ == '__main__':
    unittest.main()
