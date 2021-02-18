import unittest, sys
sys.path.append('..')
from addtwonumbers import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_add_two_numbers(self):
        ### CASE ONE
        head_one = ListNode(val=2,
                            next=ListNode(val=4,
                                          next=ListNode(val=3)))
        head_two = ListNode(val=5,
                            next=ListNode(val=6,
                                          next=ListNode(val=4)))
                            
        result = self.s.addTwoNumbers(head_one, head_two)
        self.assertEqual(result.path(), [7,0,8])
        
        
        ### CASE TWO
        head_one = ListNode(val=5)
        head_two = ListNode(val=5)
        
        result = self.s.addTwoNumbers(head_one, head_two)
        self.assertEqual(result.path(), [0,1])
        
        
        ### CASE THREE
        head_one = ListNode(val=1,
                            next = ListNode(val=8))
        head_two = ListNode(val=0)
        
        result = self.s.addTwoNumbers(head_one, head_two)
        self.assertEqual(result.path(), [1,8])
        
if __name__ == '__main__':
    unittest.main()
