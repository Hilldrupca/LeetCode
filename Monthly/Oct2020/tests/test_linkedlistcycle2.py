import unittest, sys
sys.path.append('..')
from linkedlistcycle2 import Solution, ListNode

class TestLinkedListCycle2(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_detect_cycle(self):
        case_one = ListNode(3,
                            ListNode(2,
                                     ListNode(0,
                                              ListNode(-4))))
        
        # Create cycle at node where value = 2
        case_one.next.next.next.next = case_one.next
        
        self.assertEqual(self.s.detectCycle(case_one), case_one.next)
        
        
        case_two = ListNode(1,
                            ListNode(2))
        
        # Create cycle at head node
        case_two.next.next = case_two
        
        self.assertEqual(self.s.detectCycle(case_two), case_two)
        
        
        # No cycle
        # Linked list length = 1
        case_three = ListNode(1)
        self.assertIsNone(self.s.detectCycle(case_three))
        
        
        # No cycle
        # Linked list length = 2
        case_four = ListNode(1,
                             ListNode(2))
        self.assertIsNone(self.s.detectCycle(case_four))
        
        
        # None pass as linked list
        self.assertIsNone(self.s.detectCycle(None))
        
if __name__ == '__main__':
    unittest.main()
