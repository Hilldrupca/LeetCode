import unittest, sys
sys.path.append('..')
from addtwonumbers import ListNode, Solution

class TestAddTwoNumbers(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_add_two_numbers(self):
        case_one = {'l1': ListNode(2, ListNode(4, ListNode(3))),
                    'l2': ListNode(5, ListNode(6, ListNode(4)))}
        
        self.assertEqual(self.s.addTwoNumbers(**case_one)._path(), [7,0,8])
        
        case_two = {'l1': ListNode(),
                    'l2': ListNode()}
        
        self.assertEqual(self.s.addTwoNumbers(**case_two)._path(), [0])
        
        case_three = {'l1': ListNode(9, ListNode(9, ListNode(9, ListNode(9,
                                     ListNode(9, ListNode(9, ListNode(9))))))),
                      'l2': ListNode(9, ListNode(9, ListNode(9, ListNode(9))))}
        
        self.assertEqual(self.s.addTwoNumbers(**case_three)._path(),
                         [8,9,9,9,0,0,0,1])
        
if __name__ == '__main__':
    unittest.main()
