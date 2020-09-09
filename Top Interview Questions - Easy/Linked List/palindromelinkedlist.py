
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        Determine if a linked list is a palindrome. An empty linked list
        is considered a palindrome.
        
        Params:
            head - The head node of a linked list.
            
        Returns:
            bool - Whether or not a linked list is a palindrome.
            
        Examples:
            **Assume each list is a linked list path.**
            isPalindrome([1,2])       ->   False
            isPalindrome([1,2,2,1])   ->   True
            isPalindrome([-10, -10])  ->   True
            isPalindrome([])          ->   True
        '''
        if not head:
            return True
        
        num = []
        node = head
        while node:
            num.append(node.val)
            node = node.next
            
        return num == num[::-1]
