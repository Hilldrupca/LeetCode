import unittest, sys
sys.path.append('..')
from binarytreelevelordertrav import Solution, TreeNode

class TestBinaryTreeLevelOrderTrav(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_level_order_trav(self):
        '''
                3
               / \
              9   20
                 /  \
                15   7
        '''
        case_one = TreeNode(3,
                            left=TreeNode(9),
                            right=TreeNode(20,
                                           left=TreeNode(15),
                                           right=TreeNode(7)))
        self.assertEqual(self.s.levelOrder(case_one),[[3],[9,20],[15,7]])
        
        '''
                1
               / \
              2   3
             /     \
            4       5
        '''
        case_two = TreeNode(1,
                            left=TreeNode(2,
                                          left=TreeNode(4)),
                            right=TreeNode(3,
                                           right=TreeNode(5)))
        self.assertEqual(self.s.levelOrder(case_two),[[1],[2,3],[4,5]])
        
        # Empty binary tree
        case_three = []
        self.assertEqual(self.s.levelOrder(case_three),[])
        
if __name__ == '__main__':
    unittest.main()
