import unittest, sys
sys.path.append('..')
from mapsumpairs import MapSum

class TestMapSumPairs(unittest.TestCase):
    
    def setUp(self):
        self.ms = MapSum()
        
    def test_insert(self):
        self.ms.insert('apple', 3)
        self.assertEqual(self.ms.trie['a']['p']['p']['l']['e']['*'],3)
        
        self.ms.insert('app', 2)
        self.assertEqual(self.ms.trie['a']['p']['p']['*'], 2)
        
    def test_sum(self):
        self.ms.insert('car', 1)
        self.ms.insert('cartoon', 2)
        self.ms.insert('cartridge', 3)
        self.assertEqual(self.ms.sum('car'), 6)
        self.assertEqual(self.ms.sum('cart'), 5)
        self.assertEqual(self.ms.sum('carto'), 2)
        self.assertEqual(self.ms.sum('cat'), 0)
        
if __name__ == '__main__':
    unittest.main()
