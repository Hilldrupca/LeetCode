import unittest, sys
sys.path.append('..')
from binarytreemaxdepth import Solution, TreeNode

class TestBinaryTreeMaxDepth(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_max_depth(self):
        '''
        CASE ONE
            
                3
               / \
              9   20
                 /  \
                15   7
        '''
        case_one = TreeNode(3,
                            TreeNode(9),
                            TreeNode(20,
                                     TreeNode(15),
                                     TreeNode(7)))
        
        self.assertEqual(self.s.maxDepth(case_one), 3)
        
        '''
        CASE TWO
        
                1
                 \
                  2
        '''
        case_two = TreeNode(1,
                            None,
                            TreeNode(2))
        
        self.assertEqual(self.s.maxDepth(case_two), 2)
        
        '''
        CASE THREE - empty tree
        '''
        self.assertEqual(self.s.maxDepth([]), 0)
        
        '''
        CASE FOUR - single node
        
            0
        '''
        case_four = TreeNode()
        
        self.assertEqual(self.s.maxDepth(case_four), 1)
        
if __name__ == '__main__':
    unittest.main()
