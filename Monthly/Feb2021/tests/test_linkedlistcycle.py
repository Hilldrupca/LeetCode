import unittest, sys
sys.path.append('..')
from linkedlistcycle import ListNode, Solution

class TestLinkedListCycle(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_has_cycle(self):
        '''
        CASE ONE
        
            3 -> 2 -> 0 -> -4
                 ^
                 ^
                 -4 connects here
        '''
        tail = ListNode(4)
        case_one = ListNode(3,
                            ListNode(2,
                                     ListNode(0,
                                              tail)))
        tail.next = case_one.next
        self.assertTrue(self.s.hasCycle(case_one))
        
        '''
        CASE TWO
        
            1 -> 2
            ^
            ^
            2 connects here
        '''
        tail = ListNode(2)
        case_two = ListNode(1,
                            tail)
        tail.next = case_two
        
        self.assertTrue(self.s.hasCycle(case_two))
        
        '''
        CASE THREE - single node
        
            1
        '''
        case_three = ListNode(1)
        self.assertFalse(self.s.hasCycle(case_three))
        
        '''
        CASE FOUR
        
            1 -> 2
        '''
        case_four = ListNode(1,
                             ListNode(2))
        self.assertFalse(self.s.hasCycle(case_four))
        
if __name__ == '__main__':
    unittest.main()
