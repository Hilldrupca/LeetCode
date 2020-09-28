
class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next
    
    def path(self):
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
    
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
        Rearranges in-place the linked list so that odd index elements appear
        first, followed by even index elements. 
        
        Params:
            head - The head node of a linked list.
            
        Returns:
            ListNode - The head node of the now modified linked list. None if
                       the linked list is empty.
            
        Examples:
            ***Assume lists are linked lists***
            oddEvenList([1,2,3,4,5])     ->   [1,3,5,2,4]
            oddEvenList([1,2,3,4,5,6])   ->   [1,3,5,2,4,6]
            oddEvenList([])              ->   None
        '''
        if not head:
            return
        
        odd = head
        even = even_start = head.next
        while odd.next and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        odd.next = even_start
        return head
