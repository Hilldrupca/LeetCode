import unittest, sys
sys.path.append('..')
from kthsmallestbst import Solution, TreeNode

class TestKthSmallestBst(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_kth_smallest(self):
        '''
        CASE ONE:
        
                    3
                   / \
                  1   4
                   \
                    2
        '''
        root = TreeNode(3,
                        TreeNode(1,
                                 right=TreeNode(2)),
                        TreeNode(4))
                        
        self.assertEqual(self.s.kthsmallest(root, 1), 1)
        self.assertEqual(self.s.kthsmallest(root, 2), 2)
        
        
        '''
        CASE TWO:
        
                    5
                   / \
                  3   6
                 / \
                2   4
               /
              1
        '''
        root = TreeNode(5,
                        TreeNode(3,
                                 TreeNode(2,
                                          TreeNode(1)),
                                 TreeNode(4)),
                        TreeNode(6))
                                 
        self.assertEqual(self.s.kthsmallest(root, 3), 3)
        self.assertEqual(self.s.kthsmallest(root, 6), 6)
        
        # Look for numbers out of range
        self.assertEqual(self.s.kthsmallest(root, 7), 0)
        self.assertEqual(self.s.kthsmallest(root, 0), 0)
        self.assertEqual(self.s.kthsmallest(None, 1), 0)
        
if __name__ == '__main__':
    unittest.main()
