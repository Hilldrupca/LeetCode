import unittest, sys
sys.path.append('..')
from mergesortedlinkedlists import ListNode, Solution

class TestMergeSortedLinkedLists(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
    
    def test_merge_two_lists(self):
        # two populated linked lists
        case_one = {'l1': ListNode(1, ListNode(2, ListNode(4))),
                    'l2': ListNode(1, ListNode(3, ListNode(4))),
                    }
        case_one_answer = self.s.mergeTwoLists(**case_one)
        self.assertEqual(case_one_answer._path(), [1,1,2,3,4,4])
        
        # one populated linked list
        case_two = {'l1': None,
                    'l2': ListNode(1),
                    }
        case_two_answer = self.s.mergeTwoLists(**case_two)
        self.assertEqual(case_two_answer._path(), [1])
        
        # zero populated linked lists
        case_three = {'l1': None,
                      'l2': None,
                      }
        case_three_answer = self.s.mergeTwoLists(**case_three)
        self.assertIsNone(case_three_answer)
        
if __name__ == '__main__':
    unittest.main()
