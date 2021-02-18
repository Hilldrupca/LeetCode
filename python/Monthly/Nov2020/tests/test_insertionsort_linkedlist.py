import unittest, sys
sys.path.append('..')
from insertionsort_linkedlist import Solution, ListNode

class TestInsertionSortLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_insertionSortList(self):
        '''
        CASE ONE:
            4 -> 2 -> 1 -> 3
        '''
        case_one = ListNode(4,
                            ListNode(2,
                                     ListNode(1,
                                              ListNode(3))))
                                     
        path = case_one._path()
        ans_one = self.s.insertionSortList(case_one)._path()
        self.assertEqual(path, ans_one)
        
        
        '''
        CASE TWO:
            -1 -> 5 -> 3 -> 4 -> 0
        '''
        case_two = ListNode(-1,
                            ListNode(5,
                                     ListNode(3,
                                              ListNode(3,
                                                       ListNode(0)))))
        
        path = case_two._path()
        ans_two = self.s.insertionSortList(case_two)._path()
        self.assertEqual(path, ans_two)
        
if __name__ == '__main__':
    unittest.main()
