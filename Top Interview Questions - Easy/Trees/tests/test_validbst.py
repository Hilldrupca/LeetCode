import unittest, sys
sys.path.append('..')
from validbst import Solution, TreeNode

class TestValidBST(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_validity(self):
        case_one = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
        self.assertTrue(self.s.isValidBST(case_one))
        
        case_two = TreeNode(5,
                            left=TreeNode(1),
                            right=TreeNode(4,
                                           left=TreeNode(3),
                                           right=TreeNode(6)))
        self.assertFalse(self.s.isValidBST(case_two))
        
        case_three = []
        self.assertTrue(self.s.isValidBST(case_three))
        
if __name__ == '__main__':
    unittest.main()
