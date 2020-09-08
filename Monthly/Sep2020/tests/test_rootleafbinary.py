import unittest, sys
sys.path.append('..')
from rootleafbinary import Solution, TreeNode

class TestRootLeafBinary(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().sumRootToLeaf
        
    def test_sum(self):
        '''
                        1
                       / \
                      /   \
                     0     1
                    / \   / \
                   0   1 0   1
        '''
        root = TreeNode(val=1,
                        left=TreeNode(val=0, 
                                      left=TreeNode(0),
                                      right=TreeNode(1)),
                        right=TreeNode(val=1,
                                       left=TreeNode(0),
                                       right=TreeNode(1)))
        
        self.assertEqual(self.s(root), 22)
        
if __name__ == '__main__':
    unittest.main()
