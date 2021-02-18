 
import unittest, sys
sys.path.append('..')
from linkedlistswapnodepairs import ListNode, Solution

class TestLinkedListSwapNodePairs(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_swap_pairs(self):
        '''
        CASE ONE
        
        1 -> 2 -> 3 -> 4
        '''
        case_one = ListNode(1,
                            ListNode(2,
                                     ListNode(3,
                                              ListNode(4))))
        
        case_one = self.s.swapPairs(case_one)
        self.assertEqual(case_one._path(), [2,1,4,3])
        
        '''
        CASE TWO
        
        1 -> 2 -> 3 -> 4 -> 5
        '''
        case_two = ListNode(1,
                            ListNode(2,
                                     ListNode(3,
                                              ListNode(4,
                                                       ListNode(5)))))
        
        case_two = self.s.swapPairs(case_two)
        self.assertEqual(case_two._path(), [2,1,4,3,5])
        
        '''
        CASE THREE - single node
        
        1 -> None
        '''
        case_three = ListNode(1)
        case_three = self.s.swapPairs(case_three)
        self.assertEqual(case_three._path(), [1])
        
        '''
        CASE FOUR - Empty linked list
        
        None
        '''
        case_four = None
        case_four = self.s.swapPairs(case_four)
        self.assertIsNone(case_four)
        
if __name__ == '__main__':
    unittest.main()
