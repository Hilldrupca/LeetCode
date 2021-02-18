import unittest, sys
sys.path.append('..')
from insertdeletegetrand import RandomizedSet

class TestInsertDeletegetrand(unittest.TestCase):
    
    def setUp(self):
        self.rand_set = RandomizedSet()
        
    def test_insert(self):
        self.assertTrue(self.rand_set.insert(1))
        self.assertTrue(self.rand_set.insert(2))
        
        self.assertFalse(self.rand_set.insert(1))
        
        self.assertEqual(self.rand_set.nums_list, [1,2])
        
    def test_remove(self):
        self.rand_set.insert(1)
        self.rand_set.insert(2)
        self.rand_set.insert(3)
        
        self.assertTrue(self.rand_set.remove(1))
        self.assertEqual(self.rand_set.nums_list, [3,2])
        
        self.assertFalse(self.rand_set.remove(4))
        
    def test_get_random(self):
        for x in range(10):
            self.rand_set.insert(x)
            
        for y in range(100):
            self.assertIn(self.rand_set.getRandom(),
                          self.rand_set.nums_dict)
            
if __name__ == '__main__':
    unittest.main()
