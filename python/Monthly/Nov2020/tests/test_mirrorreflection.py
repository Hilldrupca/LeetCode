import unittest, sys
sys.path.append('..')
from mirrorreflection import Solution

class TestMirrorReflection(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_mirror_reflection(self):
        case_one = {'p': 2,
                    'q': 1}
        self.assertEqual(self.s.mirrorReflection(**case_one), 2)
        
        case_two = {'p': 3,
                    'q': 2}
        self.assertEqual(self.s.mirrorReflection(**case_two), 0)
        
        case_three = {'p': 4,
                      'q': 3}
        self.assertEqual(self.s.mirrorReflection(**case_three), 2)
        
        case_four = {'p': 4,
                     'q': 2}
        self.assertEqual(self.s.mirrorReflection(**case_four), 2)
        
        case_five = {'p': 2,
                     'q': 2}
        self.assertEqual(self.s.mirrorReflection(**case_five), 1)
        
if __name__ == '__main__':
    unittest.main()
