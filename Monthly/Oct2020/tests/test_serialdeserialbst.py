import unittest, sys
sys.path.append('..')
from serialdeserialbst import Codec, TreeNode

class TestSerializeDeserializeBST(unittest.TestCase):
    
    def setUp(self):
        self.c = Codec()
        '''
                2
               / \
              1   3
        '''
        self.tree_one = TreeNode(2,
                                 TreeNode(1),
                                 TreeNode(3))
        
        '''
                3
               / \
              1   4
               \
                2
        '''
        self.tree_two = TreeNode(3,
                                 TreeNode(1,
                                          right=TreeNode(2)),
                                 TreeNode(4))
        
        '''Empty'''
        self.tree_three = None
        
        '''
                2
               /
              1
        '''
        self.tree_four = TreeNode(2, TreeNode(1))
        
        self.serial_one = '2,1,3'
        self.serial_two = '3,1,2,4'
        self.serial_three = ''
        self.serial_four = '2,1'
        
    def test_serialize(self):
        self.assertEqual(self.c.serialize(self.tree_one), self.serial_one)
        self.assertEqual(self.c.serialize(self.tree_two), self.serial_two)
        self.assertEqual(self.c.serialize(self.tree_three), self.serial_three)
        self.assertEqual(self.c.serialize(self.tree_four), self.serial_four)
        
    def test_deserialize(self):
        case_one = self.c.deserialize(self.serial_one)
        self.assertEqual(case_one.level_order(),
                         self.tree_one.level_order())
        
        case_two = self.c.deserialize(self.serial_two)
        self.assertEqual(case_two.level_order(),
                         self.tree_two.level_order())
        
        case_three = self.c.deserialize(self.serial_three)
        self.assertEqual(case_three, self.tree_three)
        
        case_four = self.c.deserialize(self.serial_four)
        self.assertEqual(case_four.level_order(),
                         self.tree_four.level_order())
        
if __name__ == '__main__':
    unittest.main()
