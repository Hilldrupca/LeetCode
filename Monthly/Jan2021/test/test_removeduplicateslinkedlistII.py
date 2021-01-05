import unittest, sys
sys.path.append('..')
from removeduplicateslinkedlistII import ListNode, Solution

class TestRemoveDuplicatesLinkedListII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_delete_duplicates(self):
        
        # Duplicates between head and tail nodes
        case_one = ListNode(1,
                            ListNode(2,
                                     ListNode(3,
                                     ListNode(3,
                                              ListNode(4,
                                              ListNode(4,
                                                       ListNode(5)))))))
                                              
        case_one = self.s.deleteDuplicates(case_one)
        self.assertEqual(case_one._path(), [1,2,5])
        
        # Duplicates at end
        case_two = ListNode(1,
                            ListNode(2,
                                     ListNode(2)))
                            
        case_two = self.s.deleteDuplicates(case_two)
        self.assertEqual(case_two._path(), [1])
        
        # Duplicates at beginning
        case_three = ListNode(1,
                              ListNode(1,
                                       ListNode(2)))
                              
        case_three = self.s.deleteDuplicates(case_three)
        self.assertEqual(case_three._path(), [2])
        
        # Single node
        case_four = ListNode(1)
        case_four = self.s.deleteDuplicates(case_four)
        self.assertEqual(case_four._path(), [1])
        
        # Empty linked list
        case_five = None
        case_five = self.s.deleteDuplicates(case_five)
        self.assertIsNone(case_five)
        
if __name__ == '__main__':
    unittest.main()
                                                                         
