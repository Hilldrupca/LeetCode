import unittest, sys
sys.path.append('..')
from streamcharacters import StreamChecker

class TestStreamCharacters(unittest.TestCase):
    
    def setUp(self):
        self.stream = StreamChecker(['cd', 'f', 'kl'])
        
    def test_equals(self):
        case_one = 'abcdefghijkl'
        answer_one = []
        for c in case_one:
            answer_one.append(self.stream.query(c))
            
        true_answer = [False, False, False, True, False, True,
                       False, False, False, False, False, True]
        
        self.assertEqual(answer_one, true_answer)

if __name__ == '__main__':
    unittest.main()
