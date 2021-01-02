import unittest, sys
sys.path.append('..')
from findnodeclonedbinarytree import Solution, TreeNode

class TestFindNodeClonedBinaryTree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_get_target_copy(self):
        '''
        CASE ONE
        
                7
               / \
              4   3 <- target
                 / \
                6   19
        '''
        case_one = TreeNode(7,
                            TreeNode(4),
                            TreeNode(3,
                                     TreeNode(6),
                                     TreeNode(19)))
                            
        case_one_clone = TreeNode(7,
                                  TreeNode(4),
                                  TreeNode(3,
                                           TreeNode(6),
                                           TreeNode(19)))
                                  
        case_one_target = case_one.right
        
        self.assertEqual(self.s.getTargetCopy(case_one,
                                              case_one_clone,
                                              case_one_target),
                         case_one_clone.right)
        
        '''
        CASE TWO
        
                8
                 \
                  6
                   \
                    5
                     \
                      4 <- target
                       \
                        3
        '''
        case_two = TreeNode(8, None,
                            TreeNode(6, None,
                                     TreeNode(5, None,
                                              TreeNode(4, None,
                                                       TreeNode(3)))))
                                              
        case_two_clone = TreeNode(8, None,
                                   TreeNode(6, None,
                                            TreeNode(5, None,
                                                     TreeNode(4, None,
                                                              TreeNode(3)))))
                                                     
        case_two_target = case_two.right.right.right
        
        self.assertEqual(self.s.getTargetCopy(case_two,
                                              case_two_clone,
                                              case_two_target),
                         case_two_clone.right.right.right)
        
        '''
        CASE THREE - single node
        
                7 <- target
        '''
        case_three = TreeNode(7)
        case_three_clone = TreeNode(7)
        case_three_target = case_three
        
        self.assertEqual(self.s.getTargetCopy(case_three,
                                              case_three_clone,
                                              case_three_target),
                         case_three_clone)
        
if __name__ == '__main__':
    unittest.main()
