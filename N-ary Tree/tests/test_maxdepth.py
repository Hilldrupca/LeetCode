import unittest, sys
sys.path.append('..')
from maxdepth import Solution, Node

class TestMaxDepth(unittest.TestCase):
    
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
                        
        self.assertEqual(self.s.maxDepth(case_one), 3)
        
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
                              
        self.assertEqual(self.s.maxDepth(case_two), 5)
        
        '''
        CASE THREE - only root
                1
        '''
        case_three = Node(1)
        self.assertEqual(self.s.maxDepth(case_three), 1)
        
        '''
        CASE FOUR - None passed as root
        '''
        case_four = None
        self.assertEqual(self.s.maxDepth(case_four), 0)
        
if __name__ == '__main__':
    unittest.main()
