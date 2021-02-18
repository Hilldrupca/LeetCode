import unittest, sys
sys.path.append('..')
from removeduplicate import Solution

class TestRemoveDuplicate(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_remove_duplicates(self):
        case_one = [1,1,2]
        self.assertEqual(self.s.removeDuplicates(case_one), 2)
        self.assertEqual(case_one, [1,2])
        
        case_two = [0,0,1,1,1,2,2,3,3,4]
        self.assertEqual(self.s.removeDuplicates(case_two), 5)
        self.assertEqual(case_two, [0,1,2,3,4])
        
if __name__ == '__main__':
    unittest.main()
