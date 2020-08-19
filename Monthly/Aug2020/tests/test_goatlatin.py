import unittest, sys
sys.path.append('..')
from goatlatin import Solution

class TestGoatLatin(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        self.assertEqual(
            self.s.toGoatLatin("I speak Goat Latin"),
                               "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
            
        self.assertEqual(
            self.s.toGoatLatin("The quick brown fox jumped over the lazy dog"),
                "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
            
if __name__ == '__main__':
    unittest.main()
