import unittest, sys
sys.path.append('..')
from reorderlist import Solution, ListNode

class TestReorderList(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        self.case_one = [ListNode(val=x) for x in range(1,5)]
        for x in range(len(self.case_one)-1):
            self.case_one[x].next = self.case_one[x+1]
            
        self.case_two = [ListNode(val=x) for x in range(1,6)]
        for x in range(len(self.case_two)-1):
            self.case_two[x].next = self.case_two[x+1]
        

        
            
    def test_equals(self):
        
        self.s.reorderList(self.case_one[0])
        self.assertEqual(self.case_one[0].order_check(), [1,4,2,3])
        
        self.s.reorderList(self.case_two[0])
        self.assertEqual(self.case_two[0].order_check(), [1,5,2,4,3])
        
if __name__ == '__main__':
    unittest.main()
