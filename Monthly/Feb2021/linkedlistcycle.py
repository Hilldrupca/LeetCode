
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for February 3rd, 2021.
    '''
    def hasCycle(self, head: ListNode) -> bool:
        '''
        Returns whether the linked list contains a cycle. Uses O(1) memory.
        
        Constraints:
            The number of nodes in the list is in the range [0, 10**4]
            -10**5 <= node.val <= 10**5
            pos is -1 or a valid index in the linked-list
            
        Params:
            head - The head node of a linked list.
            
        Returns:
            bool - Whether the linked list contains a cycle.
        '''
        if head is None or head.next is None:
            return False
        
        slow, fast = head.next, head.next.next
        
        while fast and fast.next and slow != fast:
            slow, fast = slow.next, fast.next.next
            
        if fast is None or fast.next is None:
            return False
        
        return True
