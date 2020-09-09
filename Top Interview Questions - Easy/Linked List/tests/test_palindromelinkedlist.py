import unittest, sys
sys.path.append('..')
from palindromelinkedlist import Solution, ListNode

class TestPalindromeLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_palindrome(self):
        case_one = ListNode(1, ListNode(2))
        self.assertFalse(self.s.isPalindrome(case_one))
        
        case_two = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        self.assertTrue(self.s.isPalindrome(case_two))
        
        case_three = ListNode(-10, ListNode(-10))
        self.assertTrue(self.s.isPalindrome(case_three))
        
        case_four = []
        self.assertTrue(self.s.isPalindrome(case_four))
        
if __name__ == '__main__':
    unittest.main()
