import unittest, sys
sys.path.append('..')
from addtwonumbers2 import Solution, ListNode

class TestAddTwoNumbers2(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_add_two_numbers(self):
        '''
        CASE ONE:
            l1 = 7 -> 2 -> 4 -> 3
            l2 =      5 -> 6 -> 4
                 
            sum = 7 -> 8 -> 0 -> 7
        '''
        l1 = ListNode(7,
                      ListNode(2,
                               ListNode(4,
                                        ListNode(3))))
        l2 = ListNode(5,
                      ListNode(6,
                               ListNode(4)))
                      
        ll_sum = self.s.addTwoNumbers(l1, l2)
        exp_ans = ListNode(7,
                           ListNode(8,
                                    ListNode(0,
                                             ListNode(7))))
                                    
        self.assertEqual(ll_sum, exp_ans)
        self.assertEqual(ll_sum.num_repr(), 7807)
        
        
        '''
        CASE TWO
            l1 = 2 -> 5 -> 6
            l2 =           0
                      
            sum = 2 -> 5 -> 0
        '''
        l1 = ListNode(2,
                      ListNode(5,
                               ListNode(6)))
        l2 = ListNode()
        
        ll_sum = self.s.addTwoNumbers(l1, l2)
        exp_ans = ListNode(2,
                           ListNode(5,
                                    ListNode(6)))
                           
        self.assertEqual(ll_sum, exp_ans)
        self.assertEqual(ll_sum.num_repr(), 256)
        
        
        '''
        CASE THREE
            l1 = 0
            l2 = 0
            
            sum = 0
        '''
        l1 = ListNode()
        l2 = ListNode()
        
        ll_sum = self.s.addTwoNumbers(l1, l2)
        exp_ans = ListNode()
        
        self.assertEqual(ll_sum, exp_ans)
        self.assertEqual(ll_sum.num_repr(), 0)
        
if __name__ == '__main__':
    unittest.main()
                                    
