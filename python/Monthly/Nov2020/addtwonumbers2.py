 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def num_repr(self):
        '''Returns the number the linked list represents. Used for testing.'''
        
        num = 0
        node = self
        while node:
            num = num * 10 + node.val
            node = node.next
            
        return num
    
    def __eq__(self, l2):
        '''Checks if the node values are the same as other linked list.'''
        node = self
        while node:
            try:
                if node.val == l2.val:
                    node, l2 = node.next, l2.next
                else:
                    return False
            except:
                return False
            
        return True
        
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 7th, 2020.
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Given two linked lists that represent integers, returns the sum as a
        new linked list.
        
        Params:
            l1 - A linked list representing an integer.
            
            l2 - A linked list representing an integer.
            
        Returns:
            ListNode - The head node of a linked list that is the sum of l1 and
                       l2.
                       
        Examples:
            l1 = 7 -> 2 -> 4 -> 3
            l2 = 5 -> 6 -> 4
            addTwoNumbers(l1, l2)   ->   7 -> 8 -> 0 -> 7
            
            l1 = 2 -> 5 -> 6
            l2 = 0
            addTwoNumbers(l1, l2)   ->   2 -> 5 -> 6
            
            l1 = 0
            l2 = 0
            addTwoNumbers(l1, l2)   ->   0
        
        '''
        num1 = num2 = 0
        while l1 or l2:
            if l1:
                num1 = num1 * 10 + l1.val
                l1 = l1.next
            if l2:
                num2 = num2 * 10 + l2.val
                l2 = l2.next
            
        total = num1 + num2
        res = ListNode()
        while total:
            res.val = total % 10
            total //= 10
            res = ListNode(0,res)
            
        return res.next if res.next else res
