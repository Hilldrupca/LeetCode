import unittest, sys
sys.path.append('..')
from decodestring import Solution

class TestDecodeString(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_decode_string(self):
        case_one = '3[a]2[bc]'
        self.assertEqual(self.s.decodeString(case_one), 'aaabcbc')
        
        case_two = '3[a2[c]]'
        self.assertEqual(self.s.decodeString(case_two), 'accaccacc')
        
        case_three = '2[abc]3[cd]ef'
        self.assertEqual(self.s.decodeString(case_three), 'abcabccdcdcdef')
        
        case_four = 'abc3[cd]xyz'
        self.assertEqual(self.s.decodeString(case_four), 'abccdcdcdxyz')
        
        case_five = '3[z]2[2[y]pq4[2[jk]e1[f]]]ef'
        ans = 'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'
        self.assertEqual(self.s.decodeString(case_five), ans)
        
        case_six = ''
        self.assertEqual(self.s.decodeString(case_six), '')
        
if __name__ == '__main__':
    unittest.main()
