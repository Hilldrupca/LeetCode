 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def _path(self):
        '''Used for testing.'''
        res, node = [], self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for December 24, 2020.
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        Swaps in-place every two adjacent nodes in a linked list and returns
        the (new) head node.
        
        Constraints:
            Number of nodes in linked list is in the range [0, 100]
            0 <= node.val <= 100
            
        Params:
            head - The head node of a linked list.
            
        Returns:
            ListNode - The head of the linked list after swapping node pairs.
            
        Examples:
            **Assume lists are linked lists
            swapPairs([1,2,3,4])     ->   [2,1,4,3]
            swapPairs([1,2,3,4,5])   ->   [2,1,4,3,5]
            swapPairs([1])           ->   [1]
            swapPairs([])            ->   []
        '''
        sentinel = prev = ListNode(None, head)
        one = two = sentinel
        
        while one.next and one.next.next:
            one, two = one.next, one.next.next
            prev.next, two.next, one.next = two, one, two.next
            prev = one
            
        return sentinel.next
