import unittest, sys
sys.path.append('..')
from reverselinked import Solution, ListNode

class TestReverseLinked(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_reverse(self):
        case_one = [ListNode(x) for x in range(1,6)]
        for x in range(4):
            case_one[x].next = case_one[x+1]
        
        # Check that the new head is the previous tail
        new_head = self.s.reverseList(case_one[0])
        self.assertEqual(new_head.val, case_one[-1].val)
        
        # Check for path reversal
        path = new_head.path()
        self.assertEqual(path, [5,4,3,2,1])
        
if __name__ == '__main__':
    unittest.main()
