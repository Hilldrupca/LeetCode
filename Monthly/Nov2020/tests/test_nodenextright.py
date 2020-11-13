import unittest, sys
sys.path.append('..')
from nodenextright import Solution, TreeNode

class TestNodeNextRight(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_connect(self):
        case_one = TreeNode(1,
                            TreeNode(2,
                                     TreeNode(4),
                                     TreeNode(5)),
                            TreeNode(3,
                                     TreeNode(6),
                                     TreeNode(7)))
                            
        self.s.connect(case_one)
        self.assertEqual(case_one.next_node_path(), [None,3,None,5,6,7,None])
        
if __name__ == '__main__':
    unittest.main()
