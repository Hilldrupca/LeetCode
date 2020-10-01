import unittest, sys
sys.path.append('..')
from binarytreezigzagorder import Solution, TreeNode

class TestBinaryTreeZigzagOrder(unittest.TestCase):
    
    def setUp(self):
        self.zigzag = Solution().zigzagLevelOrder
        
    def test_zigzagLevelOrder(self):
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
        
        self.assertEqual(self.zigzag(case_one), [[3],[20,9],[15,7]])
        
        
        """
        CASE TWO
                1
               / \
              2   3
             /     \
            4       5
        """
        case_two = TreeNode(1,
                            TreeNode(2,
                                     TreeNode(4)),
                            TreeNode(3,
                                     None,
                                     TreeNode(5)))
                            
        self.assertEqual(self.zigzag(case_two), [[1],[3,2],[4,5]])
        
        
        '''
        CASE THREE
                    1
                   /
                  2
                 /
                3
               /
              4
             /
            5
        '''
        case_three = TreeNode(1,
                              TreeNode(2,
                                       TreeNode(3,
                                                TreeNode(4,
                                                         TreeNode(5)))))
                                                
        self.assertEqual(self.zigzag(case_three), [[1],[2],[3],[4],[5]])
    
if __name__ == '__main__':
    unittest.main()
