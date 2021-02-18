import unittest, sys
sys.path.append('..')
from listrandompointerdeepcopy import Node, Solution

class TestListRandomPointerDeepCopy(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_copy_random_list(self):
        '''
        Numbers at bottom of vertical stacks are the random pointer values.
        The absence of a value indicates a poiner to None.
        
        '''
        
        '''
        CASE ONE
        
            7 -> 13 -> 11 -> 10 -> 1
                 7     1     11    7
        '''
        case_one = Node(7, Node(13, Node(11, Node(10, Node(1)))))
        
        case_one.next.random = case_one
        case_one.next.next.random = case_one.next.next.next.next
        case_one.next.next.next.random = case_one.next.next
        case_one.next.next.next.next.random = case_one
        
        self.assertEqual(self.s.copyRandomList(case_one)._path(),
                         case_one._path())
        
if __name__ == '__main__':
    unittest.main()
