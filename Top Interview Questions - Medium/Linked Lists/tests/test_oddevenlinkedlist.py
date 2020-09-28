import unittest, sys
sys.path.append('..')
from oddevenlinkedlist import Solution, ListNode

class TestOddEvenLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.s =  Solution()
        
    def test_odd_even_list(self):
        ### CASE ONE - odd number of elements
        head = ListNode(1,
                        ListNode(2,
                                 ListNode(3,
                                          ListNode(4,
                                                   ListNode(5)))))
                                          
        result = self.s.oddEvenList(head)
        self.assertEqual(result.path(), [1,3,5,2,4])
        
        
        ### CASE TWO - even number of elements
        head = ListNode(1,
                        ListNode(2,
                                 ListNode(3,
                                          ListNode(4,
                                                   ListNode(5,
                                                            ListNode(6))))))
                                                   
        result = self.s.oddEvenList(head)
        self.assertEqual(result.path(), [1,3,5,2,4,6])
        
        
        ### CASE THREE - empty linked list
        head = []
        self.assertIsNone(self.s.oddEvenList(head))
        
if __name__ == '__main__':
    unittest.main()
