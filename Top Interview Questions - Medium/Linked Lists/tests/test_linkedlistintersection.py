import unittest, sys
sys.path.append('..')
from linkedlistintersection import Solution, ListNode

class TestLinkedListIntersection(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_get_intersection_node(self):
        '''
        CASE ONE - unique integers used
        
                 1 -> 2
                       \
                        6 -> 7 -> 8
                       /
            3 -> 4 -> 5
        
        '''
        ll_one = headA = ListNode(1)
        ll_one.next = ListNode(2)
        ll_one = ll_one.next
        
        ll_two = headB = ListNode(3)
        ll_two.next = ListNode(4)
        ll_two = ll_two.next
        ll_two.next = ListNode(5)
        
        ll_one.next = ll_two.next = result = ListNode(6,
                                                      ListNode(7,
                                                               ListNode(8)))
                                                      
        self.assertEqual(self.s.getIntersectionNode(headA, headB), result)
        
        
        '''
        CASE TWO - repeat integers, but unique ListNode's
        
        4 -> 9 -> 1
                   \
                    2 -> 4
                   /
                  1
        '''
        ll_one = headA = ListNode(4)
        ll_one.next = ListNode(9)
        ll_one = ll_one.next
        ll_one.next = ListNode(1)
        ll_one = ll_one.next
        
        ll_two = headB = ListNode(1)
        
        ll_one.next = ll_two.next = result = ListNode(2,
                                                      ListNode(4))
        
        self.assertEqual(self.s.getIntersectionNode(headA, headB), result)
        
        
        '''
        CASE THREE - no intersection
        
        2 -> 6 -> 4
        
             1 -> 5
        '''
        headA = ListNode(2,
                         ListNode(6,
                                  ListNode(4)))
        headB = ListNode(1,
                         ListNode(5))
        
        self.assertIsNone(self.s.getIntersectionNode(headA, headB))
        
if __name__ == '__main__':
    unittest.main()
