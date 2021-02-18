import unittest, sys
sys.path.append('..')
from removeduplicate import Solution

class TestRemoveDuplicates(unittest.TestCase):
     
    def setUp(self):
        self.s = Solution()
         
    def test_equals(self):
        case_one = [1,1,2]
        case_one_index = self.s.removeDuplicates(case_one)
        self.assertEqual(case_one[:case_one_index], [1,2])
        
        case_two = [0,0,1,1,1,2,2,3,3,4]
        case_two_index = self.s.removeDuplicates(case_two)
        self.assertEqual(case_two[:case_two_index], [0,1,2,3,4])
        
if __name__ == '__main__':
    unittest.main()
        
        
