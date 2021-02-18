import unittest, sys
sys.path.append('..')
from minstack import MinStack

class TestMinStack(unittest.TestCase):
    
    def setUp(self):
        self.stack = MinStack()
        self.stack.push(2)
        self.stack.push(1)
        
    def test_push(self):
        self.stack.push(3)
        self.assertEqual(self.stack.stack[-1], 3)
        
    def test_pop(self):
        self.stack.pop()
        self.assertEqual(self.stack.stack[-1], 2)
        
    def test_top(self):
        self.assertEqual(self.stack.top(), 1)
        
    def test_getMin(self):
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.push(-1000)
        self.assertEqual(self.stack.getMin(), -1000)
        
if __name__ == '__main__':
    unittest.main()
