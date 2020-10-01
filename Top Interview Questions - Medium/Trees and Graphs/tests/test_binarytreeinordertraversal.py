import unittest, sys
sys.path.append('..')
from binarytreeinordertraversal import Solution, TreeNode

class TestBinaryTreeInorderTraversal(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_inorder_traversal(self):
        '''
            1
             \
              2
             /
            3
        '''
        case_one = TreeNode(val=1,
                            right=TreeNode(val=2,
                                           left=TreeNode(3)))
                            
        self.assertEqual(self.s.inorderTraversal(case_one), [1,3,2])
        
        
        '''
            1
           /
          2
        '''
        case_two = TreeNode(val=1,
                            left=TreeNode(2))
        
        self.assertEqual(self.s.inorderTraversal(case_two), [2,1])
        
        
        '''
            1
             \
              2
        '''
        case_three = TreeNode(val=1,
                              right=TreeNode(2))
        
        self.assertEqual(self.s.inorderTraversal(case_three), [1,2])
        
        
        # Empty root node
        self.assertEqual(self.s.inorderTraversal([]), [])
        
if __name__ == '__main__':
    unittest.main()
