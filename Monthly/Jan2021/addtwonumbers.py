
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
       
    def _path(self):
        '''Helper function. Used to ensure correct path.'''
        res, node = [], self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 12th, 2021.
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Given two non-empty linked lists representing non-negative integers in
        reverse order, returns the sum also in reversed order. Given the linked
        lists representing 100 (0 -> 0 -> 1), and 900 (0 -> 0 -> 9), the
        returned linked list would look like 0 -> 0 -> 0 -> 1.
        
        Constraints:
            - The number of nodes in each linked list is in the range [1, 100]
            - 0 <= node.val <= 9
            - It is guaranteed that the list represents a number that does not 
              have leading zeroes
              
        Params:
            l1 - The head node of a linked list representing a non-negative
                 integer in reverse order.
                 
            l2 - The head node of a linked list representing a non-negative
                 integer in reverse order.
                 
        Returns:
            ListNode - The head node of a linked list representing the sum of
                       l1 and l2 (also in reverse order).
                       
        Examples:
            ** Assume all lists are linked lists **
            addTwoNumbers([2,4,3],[5,6,4])   ->   [7,0,8]
            addTwoNumbers([0],[0])           ->   [0]
            addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])   ->   [8,9,9,9,0,0,0,1]
        '''
        sentinel = node = ListNode()
        while l1 or l2:
            if l1:
                l1, node.val = l1.next, node.val + l1.val
                
            if l2:
                l2, node.val = l2.next, node.val + l2.val
                
            tens = node.val // 10
            if l1 or l2 or tens:
                node.next = ListNode(tens)
                
            node.val, node = node.val % 10, node.next            
            
        return sentinel
