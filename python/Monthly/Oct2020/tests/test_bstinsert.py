import unittest, sys
sys.path.append('..')
from bstinsert import Solution, TreeNode

class TestBstInsert(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_insert_into_bst(self):
        '''
        CASE ONE
        
                    4
                   / \
                  2   7
                 / \
                1   3
        '''
        case_one = TreeNode(4,
                            TreeNode(2,
                                     TreeNode(1),
                                     TreeNode(3)),
                            TreeNode(7))
                            
        self.s.insertIntoBST(case_one, 5)
        self.assertEqual(case_one.level_order(), [4,2,7,1,3,5,None])
        
        
        '''
        CASE TWO
        
                    40
                   /  \
                  /    \
                20      60
               /  \    /  \
              10  30  50  70
        '''
        case_two = TreeNode(40,
                            TreeNode(20,
                                     TreeNode(10),
                                     TreeNode(30)),
                            TreeNode(60,
                                     TreeNode(50),
                                     TreeNode(70)))
        
        self.s.insertIntoBST(case_two, 15)
        self.assertEqual(case_two.level_order(), [40,20,60,10,30,50,70,None,15])
        
        
        '''
        CASE THREE - empty tree
                []
        '''
        case_three = self.s.insertIntoBST([], 2)
        self.assertEqual(case_three.level_order(), [2])
        
if __name__ == '__main__':
    unittest.main()
