import unittest, sys
sys.path.append('..')
from linkedlistcycle import Solution, ListNode

class TestLinkedListCycle(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_cycle(self):
        case_one = ListNode(3, ListNode(2, ListNode(0, ListNode(4))))
        case_one.next.next.next.next = case_one
        self.assertTrue(self.s.hasCycle(case_one))
        
        case_two = ListNode(1, ListNode(2))
        case_two.next.next = case_two
        self.assertTrue(self.s.hasCycle(case_two))
        
        case_three = ListNode(1)
        self.assertFalse(self.s.hasCycle(case_three))
        
if __name__ == '__main__':
    unittest.main()
