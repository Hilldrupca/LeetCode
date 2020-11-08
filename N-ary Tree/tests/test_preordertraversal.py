import unittest, sys
sys.path.append('..')
from preordertraversal import Solution, Node

class TestPreorderTraversal(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_preorder(self):
        '''
        CASE ONE
                1
               /|\
              3 2 4
             / \
            5   6
        '''
        case_one = Node(1,
                        [Node(3,
                              [Node(5), Node(6)]),
                         Node(2),
                         Node(4)])
                        
        self.assertEqual(self.s.preorder(case_one), [1,3,5,6,2,4])
        
        '''
        CASE TWO
                ____1_____
               /   / \    \
              /   /   \    \
             2   3     4    5
                / \    |   / \
               6   7   8  9   10
                   |   |  |
                  11  12  13
                   |
                  14
        '''
        case_two = Node(1,
                        [Node(2),
                         Node(3,
                              [Node(6),
                               Node(7,
                                    [Node(11,
                                          [Node(14)])])]),
                         Node(4,
                              [Node(8,
                                    [Node(12)])]),
                         Node(5,
                              [Node(9,
                                    [Node(13)]),
                               Node(10)])])
                              
        self.assertEqual(self.s.preorder(case_two),
                         [1,2,3,6,7,11,14,4,8,12,5,9,13,10])
        
        '''
        CASE THREE - only root
                1
        '''
        case_three = Node(1)
        self.assertEqual(self.s.preorder(case_three), [1])
        
        '''
        CASE FOUR - None passed as root
        '''
        case_four = None
        self.assertEqual(self.s.preorder(case_four), [])
        
if __name__ == '__main__':
    unittest.main()
        
