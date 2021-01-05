
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def _path(self):
        '''Helper function. Used for testing correct path after deletion.'''
        res, node = [], self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 5th, 2021.
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        Given the head node of a sorted linked list, returns a linked list with
        all nodes that have duplicate numbers removed.
        
        Constraints:
            The number of nodes in the list is in the range [0, 300]
            -100 <= Node.val <= 100
            The list is guaranteed to be sorted in ascending order
            
        Params;
            head - The head node of a linked list sorted in ascending order.
            
        Returns:
            ListNode - A linked list with duplicate number nodes removed, and
                       sorted in ascending order.
                       
        Examples:
            ** Assume lists are linked lists **
            deleteDuplicates([1,2,3,3,4,4,5])   ->   [1,2,5]
            deleteDuplicates([1,2,2])           ->   [1]
            deleteDuplicates([1,1])             ->   []
            deleteDuplicates([1])               ->   [1]
        '''
        sentinel = prev = ListNode()
        while head:
            dup = False
            while head.next and head.val == head.next.val:
                head = head.next
                dup = True
                
            if dup:
                prev.next = None
                head = head.next
            else:
                prev.next, head = head, head.next
                prev = prev.next
                
        return sentinel.next
