import unittest, sys
sys.path.append('..')
from binarytreetilt import Solution, TreeNode

class TestBinaryTreeTilt(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_tilt_(self):
        '''
        CASE ONE
                1
               / \
              2   3
        '''
        case_one = TreeNode(1,
                            TreeNode(2),
                            TreeNode(3))
        self.assertEqual(self.s.findTilt(case_one), 1)
        
        '''
        CASE TWO
                    4
                   / \
                  2   9
                 / \   \
                3   5   7
        '''
        case_two = TreeNode(4,
                            TreeNode(2,
                                     TreeNode(3),
                                     TreeNode(5)),
                            TreeNode(9,
                                     None,
                                     TreeNode(7)))
        self.assertEqual(self.s.findTilt(case_two), 15)
        
        '''
        CASE THEE
                        21
                       /  \
                      7    14
                     / \   / \
                    1   1 2   2
                   / \
                  3   3
        '''
        case_three = TreeNode(21,
                              TreeNode(7,
                                       TreeNode(1,
                                                TreeNode(3),
                                                TreeNode(3)),
                                       TreeNode(1)),
                              TreeNode(14,
                                       TreeNode(2),
                                       TreeNode(2)))
        self.assertEqual(self.s.findTilt(case_three), 9)
        
        '''
        CASE FOUR - empty tree
        '''
        case_four = TreeNode(1)
        self.assertEqual(self.s.findTilt(case_four), 0)
        
        '''
        CASE FIVE - None passed as tree
        '''
        case_five = None
        self.assertEqual(self.s.findTilt(case_five), 0)
        
if __name__ == '__main__':
    unittest.main()
        
        
