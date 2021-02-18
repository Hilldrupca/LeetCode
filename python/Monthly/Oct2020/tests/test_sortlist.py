import unittest, sys
sys.path.append('..')
from sortlist import Solution, ListNode

class TestSortList(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_sort_list(self):
        '''
        CASE ONE - even number of nodes.
        
        4 -> 2 -> 1 -> 3
        '''
        case_one = ListNode(4,
                            ListNode(2,
                                     ListNode(1,
                                              ListNode(3))))
                                     
        case_one = self.s.sortList(case_one)
        self.assertEqual(case_one._path(), [1,2,3,4])
        
        
        '''
        CASE TWO - odd number of nodes.
        
        71 -> 20 -> -3 -> 0 -> 5
        '''
        case_two = ListNode(71,
                            ListNode(20,
                                     ListNode(-3,
                                              ListNode(0,
                                                       ListNode(5)))))
                                    
        case_two = self.s.sortList(case_two)
        self.assertEqual(case_two._path(), [-3,0,5,20,71])
        
        
        '''
        CASE THREE - empty linked list.
        '''
        case_three = None
        case_three = self.s.sortList(case_three)
        self.assertIsNone(case_three)
        
if __name__ == '__main__':
    unittest.main()
