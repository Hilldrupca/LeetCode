import unittest, sys
sys.path.append('..')
from trimbst import Solution, TreeNode

class TestTrimBST(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_trim_bst(self):
        '''
        CASE ONE
        
                1
               / \
              0   2
        '''
        case_one = {'root': TreeNode(1,
                                     TreeNode(0),
                                     TreeNode(2)),
                    'low': 1,
                    'high': 2}
        
        self.assertEqual(self.s.trimBST(**case_one)._inorder_traversal(),
                           [1, 2])
        
        '''
        CASE TWO
        
                3
               / \
              0   4
               \
                2
               /
              1
        '''
        case_two = {'root': TreeNode(3,
                                     TreeNode(0,
                                              None,
                                              TreeNode(2,
                                                       TreeNode(1))),
                                     TreeNode(4)),
                    'low': 1,
                    'high': 3}
        
        self.assertEqual(self.s.trimBST(**case_two)._inorder_traversal(),
                           [3, 2, 1])
        
        '''
        CASE THREE - single node
        
                1
        '''
        case_three = {'root': TreeNode(1),
                      'low': 1,
                      'high': 2}
        
        self.assertEqual(self.s.trimBST(**case_three)._inorder_traversal(),
                           [1])
        
        '''
        CASE FOUR
        
                1
                 \
                  2
        '''
        case_four = {'root': TreeNode(1,
                                      None,
                                      TreeNode(2)),
                     'low': 1,
                     'high': 3}
        
        self.assertEqual(self.s.trimBST(**case_four)._inorder_traversal(),
                           [1, 2])
        
        '''
        CASE FIVE
        
                1
                 \
                  2
        '''
        case_five = {'root': TreeNode(1,
                                      None,
                                      TreeNode(2)),
                     'low': 2,
                     'high': 4}
        
        self.assertEqual(self.s.trimBST(**case_five)._inorder_traversal(),
                         [2])
        
if __name__ == '__main__':
    unittest.main()
