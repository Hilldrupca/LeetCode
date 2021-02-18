import unittest, sys
sys.path.append('..')
from groupanagrams import Solution

class TestGroupAnagrams(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_group_anagrams(self):
        case_one = ["eat","tea","tan","ate","nat","bat"]
        ans_one = self.s.groupAnagrams(case_one)
        answers_by_len = {1: ['bat'],
                          2: ['nat','tan'],
                          3: ['ate','eat','tea']}
        all_in = False
        for x in ans_one:
            all_in = set(x) == set(answers_by_len[len(x)])
            
        self.assertTrue(all_in)
        
        
        case_two = ['']
        self.assertEqual(self.s.groupAnagrams(case_two), [['']])
        
        case_three = ['a']
        self.assertEqual(self.s.groupAnagrams(case_three), [['a']])
        
if __name__ == '__main__':
    unittest.main()
