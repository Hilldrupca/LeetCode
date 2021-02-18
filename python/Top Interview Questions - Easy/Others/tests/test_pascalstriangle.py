import unittest, sys
sys.path.append('..')
from pascalstriangle import Solution

class TestPascalsTriangle(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_generate(self):
        ans_one = [[1],
                   [1,1],
                   [1,2,1],
                   [1,3,3,1],
                   [1,4,6,4,1]]
        self.assertEqual(self.s.generate(5), ans_one)
        
        ans_two = [[1],
                   [1,1],
                   [1,2,1],
                   [1,3,3,1],
                   [1,4,6,4,1],
                   [1,5,10,10,5,1],
                   [1,6,15,20,15,6,1],
                   [1,7,21,35,35,21,7,1]]
        self.assertEqual(self.s.generate(8), ans_two)
        
        self.assertEqual(self.s.generate(0), [])
        
if __name__ == '__main__':
    unittest.main()
