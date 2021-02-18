import unittest, sys
sys.path.append('..')
from mergelinkedlist import Solution, ListNode

class TestMergeLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().mergeTwoLists
        self.linked_list_one = ListNode(1,ListNode(2,ListNode(4)))
        self.linked_list_two = ListNode(1,ListNode(3, ListNode(4)))
        
    def test_merge_both_populated(self):
        path = self.s(self.linked_list_one,
                               self.linked_list_two)
        path = path.path()
        self.assertEqual(path, [1,1,2,3,4,4])
        
    def test_merge_one_populated(self):
        path_one = self.s(self.linked_list_one, [])
        path_one = path_one.path()
        self.assertEqual(path_one, [1,2,4])
        
        path_two = self.s([],
                          self.linked_list_two)
        path_two = path_two.path()
        self.assertEqual(path_two, [1,3,4])
        
    def test_merge_empty(self):
        path = self.s([], [])
        self.assertEqual(path, [])
        
if __name__ == '__main__':
    unittest.main()
