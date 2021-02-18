import unittest, sys
sys.path.append('..')
from houserobberIII import Solution, TreeNode

class TestHouseRobberIII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_rob(self):
        '''
        CASE ONE:
        
                3
               / \
              2   3
               \   \
                3   1
        '''
        case_one = TreeNode(3,
                            TreeNode(2,
                                     None,
                                     TreeNode(3)),
                            TreeNode(3,
                                     None,
                                     TreeNode(1)))
        self.assertEqual(self.s.rob(case_one), 7)
        
        '''
        CASE TWO:
        
                3
               / \
              4   5
             / \   \
            1   3   1
        '''
        case_two = TreeNode(3,
                            TreeNode(4,
                                     TreeNode(1),
                                     TreeNode(3)),
                            TreeNode(5,
                                     None,
                                     TreeNode(1)))
        self.assertEqual(self.s.rob(case_two), 9)
        
        # Empty tree passed
        self.assertEqual(self.s.rob(None), 0)
        
if __name__ == '__main__':
    unittest.main()
