import unittest, sys
sys.path.append('..')
from binarytreeverticalorder import Solution, TreeNode

class TestBinaryTreeVerticalOrder(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_vertical_traversal(self):
        '''
        CASE ONE
        
                3
               / \
              9  20
                /  \
               15   7
        '''
        case_one = TreeNode(3,
                            TreeNode(9),
                            TreeNode(20,
                                     TreeNode(15),
                                     TreeNode(7)))
        
        self.assertEqual(self.s.verticalTraversal(case_one),
                         [[9], [3,15], [20], [7]])
        
        
        '''
        CASE TWO
        
                 1
               /   \
              2     3
             / \   / \
            4   5 6   7
        '''
        case_two = TreeNode(1,
                            TreeNode(2,
                                     TreeNode(4),
                                     TreeNode(5)),
                            TreeNode(3,
                                     TreeNode(6),
                                     TreeNode(7)))
                            
        self.assertEqual(self.s.verticalTraversal(case_two),
                         [[4], [2], [1,5,6], [3], [7]])
        
if __name__ == '__main__':
    unittest.main()
