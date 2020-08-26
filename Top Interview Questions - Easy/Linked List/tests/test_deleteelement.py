import unittest, sys
sys.path.append('..')
from deleteelement import Solution, ListNode

class TestDeleteElement(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = [ListNode(x) for x in range(1,6)]
        for x in range(4):
            case_one[x].next = case_one[x+1]
        
        head_one = self.s.removeNthFromEnd(case_one[0], 2)
        
        self.assertEqual(head_one, ListNode(1)) # Check for correct head node
        self.assertEqual(head_one.path(), [1,2,3,5]) # Check path
        
        case_two = ListNode(1)
        head_two = self.s.removeNthFromEnd(case_two, 1)
        
        self.assertEqual(head_two, None) # Check if only element deleted
        
if __name__ == '__main__':
    unittest.main()
