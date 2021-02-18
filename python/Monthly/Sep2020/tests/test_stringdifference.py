import unittest, sys
sys.path.append('..')
from stringdifference import Solution

class TestStringDifference(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_the_difference(self):
        self.assertEqual(self.s.findTheDifference(s='abcd',
                                                  t='abcde'), 'e')
        
        self.assertEqual(self.s.findTheDifference(s='rawr',
                                                  t='brawr'), 'b')
        
if __name__ == '__main__':
    unittest.main()
