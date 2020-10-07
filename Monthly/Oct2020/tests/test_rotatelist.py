import unittest, sys
sys.path.append('..')
from rotatelist import Solution, ListNode

class TestRotateList(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_rotate_right(self):
        case_one = ListNode(1,
                            ListNode(2,
                                     ListNode(3,
                                              ListNode(4,
                                                       ListNode(5)))))
        case_one = self.s.rotateRight(case_one, 2)
        self.assertEqual(case_one._path(), [4,5,1,2,3])
        
        
        case_two = ListNode(0,
                            ListNode(1,
                                     ListNode(2)))
                            
        case_two = self.s.rotateRight(case_two, 4)
        self.assertEqual(case_two._path(), [2,0,1])
        
        
        case_three = ListNode(1, ListNode(2))
        case_three = self.s.rotateRight(case_three, 1)
        self.assertEqual(case_three._path(), [2,1])
        
if __name__ == '__main__':
    unittest.main()
