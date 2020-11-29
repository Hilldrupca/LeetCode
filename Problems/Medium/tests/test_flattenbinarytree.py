import unittest, sys
sys.path.append('..')
from flattenbinarytree import Solution, TreeNode

class TestFlattenBinaryTree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_flatten(self):
        '''
        CASE ONE:
        
                1
               / \
              2   5
             / \   \
            3   4   6
        '''
        case_one = TreeNode(1,
                            TreeNode(2,
                                     TreeNode(3),
                                     TreeNode(4)),
                            TreeNode(5,
                                     None,
                                     TreeNode(6)))
        self.s.flatten(case_one)
        self.assertEqual(case_one._path(),
                         [1,None,2,None,3,None,4,None,5,None,6])
        
        '''
        CASE TWO
        
                6
               / \
              5   4
             / \   \
            3   2   1
        '''
        case_two = TreeNode(6,
                            TreeNode(5,
                                     TreeNode(3),
                                     TreeNode(2)),
                            TreeNode(4,
                                     None,
                                     TreeNode(1)))
        self.s.flatten(case_two)
        self.assertEqual(case_two._path(),
                         [6,None,5,None,3,None,2,None,4,None,1])
        
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
        self.s.flatten(case_three)
        self.assertEqual(case_three._path(),
                         [1,None,2,None,3,None,4,None,5])
        
        '''
        CASE FOUR - single node
        
                1
        '''
        case_four = TreeNode(1)
        self.s.flatten(case_four)
        self.assertEqual(case_four._path(), [1])
        
        '''
        CASE FIVE - empty tree
        '''
        case_five = None
        self.s.flatten(case_five)
        self.assertIsNone(case_five)
        
if __name__ == '__main__':
    unittest.main()
