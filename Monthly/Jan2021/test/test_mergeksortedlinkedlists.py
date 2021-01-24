import unittest, sys
sys.path.append('..')
from mergeksortedlinkedlists import ListNode, Solution

class TestMergeKSortedLinkedLists(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_merge_k_lists(self):
        '''
        Linked lists:
        
            1 -> 4 -> 5
            1 -> 3 -> 4
            2 -> 6
        '''
        case_one = [ListNode(1, ListNode(4, ListNode(5))),
                    ListNode(1, ListNode(3, ListNode(4))),
                    ListNode(2, ListNode(6))]
        
        self.assertEqual(self.s.mergeKLists(case_one)._path(),
                         [1,1,2,3,4,4,5,6])
        
        '''
        None passed
        '''
        case_two = None
        self.assertIsNone(self.s.mergeKLists(case_two))
        
        '''
        One empty linked list (None) passed
        '''
        case_three = [None]
        self.assertIsNone(self.s.mergeKLists(case_three))
        
if __name__ == '__main__':
    unittest.main()
