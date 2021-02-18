import unittest, sys
sys.path.append('..')
from randomlinkedlistnode import ListNode, Solution

class TestRandomLinkedListNode(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution(ListNode(1,
                                   ListNode(2,
                                            ListNode(3))))
        
    def test_get_random(self):
                            
        for _ in range(10):
            self.assertIn(self.s.getRandom(),[1,2,3])
            
if __name__ == '__main__':
    unittest.main()
