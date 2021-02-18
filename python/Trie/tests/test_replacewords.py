import unittest, sys
sys.path.append('..')
from replacewords import Solution

class TestReplaceWords(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_replace_words(self):
        case_one = {'dictionary': ['cat','bat','rat'],
                    'sentence': 'the cattle was rattled by the battery'}
        self.assertEqual(self.s.replaceWords(**case_one),
                         'the cat was rat by the bat')
        
        case_two = {'dictionary': ['a','b','c'],
                    'sentence': 'aadsfasf absbs bbab cadsfafs'}
        self.assertEqual(self.s.replaceWords(**case_two),
                         'a a b c')
        
        case_three = {'dictionary': ['a', 'aa', 'aaa', 'aaaa'],
                      'sentence': 'a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa'}
        self.assertEqual(self.s.replaceWords(**case_three),
                         'a a a a a a a a bbb baba a')
        
        case_four = {'dictionary': ['catt','cat','bat','rat'],
                     'sentence': 'the cattle was rattled by the battery'}
        self.assertEqual(self.s.replaceWords(**case_four),
                         'the cat was rat by the bat')
        
        case_five = {'dictionary': ['ac','ab'],
                     'sentence': 'it is abnormal that this solution is accepted'}
        self.assertEqual(self.s.replaceWords(**case_five),
                         'it is ab that this solution is ac')
        
        # Empty dictionary
        case_six = {'dictionary': [],
                    'sentence': 'Dictionaries are useful'}
        self.assertEqual(self.s.replaceWords(**case_six),
                         'Dictionaries are useful')
        
        # Empty sentence
        case_seven = {'dictionary': ['a','b'],
                      'sentence': ''}
        self.assertEqual(self.s.replaceWords(**case_seven), '')
        
if __name__ == '__main__':
    unittest.main()
