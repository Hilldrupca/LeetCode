import unittest, sys
sys.path.append('..')
from bstiterator import BSTIterator, TreeNode

class TestBSTIterator(unittest.TestCase):
        
    def test_next_hasNext(self):
        '''
        Binary search tree:
        
                7
               / \
              3   15
                 /  \
                9    20
        '''
        bst_iter = BSTIterator(TreeNode(7,
                                        TreeNode(3),
                                        TreeNode(15,
                                                 TreeNode(9),
                                                 TreeNode(20))))
                                        
        '''
        Order of calls, and expected returns:
        
        next()    = 3
        next()    = 7
        hasNext() = True
        next()    = 9
        hasNext() = True
        next()    = 15
        hasNext() = True
        next()    = 20
        hasNext() = False
        '''
        funcs = [bst_iter.next, bst_iter.next, bst_iter.hasNext,
                 bst_iter.next, bst_iter.hasNext, bst_iter.next,
                 bst_iter.hasNext, bst_iter.next, bst_iter.hasNext]
                        
        exp_answers = [3,7,True,9,True,15,True,20,False]
        
        for f, ans in zip(funcs, exp_answers):
            with self.subTest(call=f, answer=ans):
                self.assertEqual(f(), ans)
                
        # iterator should be exhausted at this point
        with self.assertRaises(StopIteration):
            bst_iter.next()
            
if __name__ == '__main__':
    unittest.main()
        
