import unittest, sys
sys.path.append('..')
from minbinarytreedepth import Solution, TreeNode

class TestMinBinaryTreeDepth(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_min_depth(self):
        '''
        CASE ONE:
                 3
                / \
               9   20
                  /  \
                15    7
        '''
        case_one = TreeNode(3,
                            TreeNode(9),
                            TreeNode(20,
                                     TreeNode(15),
                                     TreeNode(7)))
                            
        self.assertEqual(self.s.minDepth(case_one), 2)
        self.assertEqual(self.s.minDepthRecursive(case_one), 2)
        
        
        '''
        CASE TWO:
                2
                 \
                  3
                   \
                    4
                     \
                      5
                       \
                        6
        '''
        case_two = TreeNode(2,
                            None,
                            TreeNode(3,
                                     None,
                                     TreeNode(4,
                                              None,
                                              TreeNode(5,
                                                       None,
                                                       TreeNode(6)))))
        
        self.assertEqual(self.s.minDepth(case_two), 5)
        self.assertEqual(self.s.minDepthRecursive(case_two), 5)
        
        
        # Empty tree
        self.assertEqual(self.s.minDepth(None), 0)
        self.assertEqual(self.s.minDepthRecursive(None), 0)
        
if __name__ == '__main__':
    unittest.main()
