
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for October 27th, 2020.
    '''
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        If it exists, returns the node where a cycle in a linked list begins.
        
        Params:
            head - The head node of a linked list.
            
        Returns:
            ListNode - The node where the cycle begins. Returns None if no
                       cycle exists.
                       
        Examples:
            
                          <------------
                          v           ^
            l_list = 3 -> 2 -> 0 -> 4 ^
            detectCycle(l_list)   ->   2
            
            l_list = 1 -> 2 -> 3
            detectCycle(l_list)   ->   None
        '''
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                    
                return slow
            
        return None
