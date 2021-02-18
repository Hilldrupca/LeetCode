import unittest, sys
sys.path.append('..')
from maxdepthbinarytree import Solution, TreeNode

class TestMaxDepthBinaryTree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_depth(self):
        case_one = TreeNode(3,
                            left=TreeNode(9),
                            right=TreeNode(20,
                                           left=TreeNode(15),
                                           right=TreeNode(7)))
                            
        self.assertEqual(self.s.maxDepth(case_one), 3)
        
        case_two = TreeNode(3)
        self.assertEqual(self.s.maxDepth(case_two), 1)
        
        case_three = []
        self.assertEqual(self.s.maxDepth(case_three), 0)
        
if __name__ == '__main__':
    unittest.main()
