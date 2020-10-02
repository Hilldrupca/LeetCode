import unittest, sys
sys.path.append('..')
from binarytreenextright import Solution, TreeNode

class TestBinaryTreeNextRight(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_binary_tree_next_right(self):
        '''
                        1
                       / \
                      /   \
                     2     3
                    / \   / \
                   4   5 6   7
        '''
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(4),
                                 TreeNode(5)),
                        TreeNode(3,
                                 TreeNode(6),
                                 TreeNode(7)))
                        
        self.assertEqual(self.s.connect(root).path(), [[1],
                                                       [2,3],
                                                       [4,5,6,7]])
        
if __name__ == '__main__':
    unittest.main()
