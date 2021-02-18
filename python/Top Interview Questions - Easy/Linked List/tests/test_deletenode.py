import unittest, sys
sys.path.append('..')
from deletenode import Solution, ListNode

class TestDeleteNode(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_deletion(self):
        case_one = [ListNode(x) for x in [4,5,1,9]]
        for x in range(len(case_one)-1):
            case_one[x].next = case_one[x+1]
            
        # Delete node 5
        self.s.deleteNode(case_one[1])
        self.assertEqual(case_one[0].path(), [4,1,9])
        
        case_two = [ListNode(x) for x in [4,5,1,9]]
        for x in range(len(case_two)-1):
            case_two[x].next = case_two[x+1]
            
        # Attempt to delete tail (node 9)
        self.s.deleteNode(case_two[-1])
        self.assertEqual(case_two[0].path(), [4,5,1,9])
        
        
if __name__ == '__main__':
    unittest.main()
