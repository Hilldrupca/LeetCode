import unittest, sys
sys.path.append('..')
from bst2greatertree import Solution, TreeNode

class TestBst2GreaterTree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_convert_bst(self):
        '''
        CASE ONE
        
                _4_
               /   \
              1     6
             / \   / \
            0   2 5   7
                 \     \
                  3     8
        '''
        case_one = TreeNode(4,
                            TreeNode(1,
                                     TreeNode(0),
                                     TreeNode(2,
                                              None,
                                              TreeNode(3))),
                            TreeNode(6,
                                     TreeNode(5),
                                     TreeNode(7,
                                              None,
                                              TreeNode(8))))
                                     
        self.assertEqual(self.s.convertBST(case_one)._path(),
                         [30,36,21,36,35,26,15,33,8])
        
        '''
        CASE TWO
        
                0
                 \
                  1
        '''
        case_two = TreeNode(0, None, TreeNode(1))
        
        self.assertEqual(self.s.convertBST(case_two)._path(), [1,1])
        
        '''
        CASE THREE
        
                1
               / \
              0   2
        '''
        case_three = TreeNode(1,
                              TreeNode(),
                              TreeNode(2))
        
        self.assertEqual(self.s.convertBST(case_three)._path(), [3,3,2])
        
        '''
        CASE FOUR
        
                3
               / \
              2   4
             /
            1
        '''
        case_four = TreeNode(3,
                             TreeNode(2,
                                      TreeNode(1)),
                             TreeNode(4))
                             
        self.assertEqual(self.s.convertBST(case_four)._path(), [7,9,4,10])
        
        '''
        CASE FIVE - single node
        
                1
        '''
        case_five = TreeNode(1)
        
        self.assertEqual(self.s.convertBST(case_five)._path(), [1])
        
        '''
        CASE SIX - Empty tree
        '''
        case_six = None
        
        self.assertIsNone(self.s.convertBST(case_six))
        
if __name__ == '__main__':
    unittest.main()
