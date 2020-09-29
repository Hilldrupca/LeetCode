 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        '''
        Returns the intersection of two singly linked lists if it exists.
        
        Params:
            headA, headB - Linked list head nodes.
            
        Returns:
            ListNode - The node where two linked lists intersect. Returns None
                       if there is no intersection.
                       
        Example:
            Given the following linked lists:
        
                 1 -> 2
                       \
                        6 -> 7 -> 8
                       /
            3 -> 4 -> 5
            
            getIntersection(1, 3) would return node 6
        '''
        if not headA or not headB:
            return None
        
        # Get the lengths of each linked list
        l1_len = l2_len = 0
        l1, l2 = headA, headB
        while l1.next:
            l1_len += 1
            l1 = l1.next
            
        while l2.next:
            l2_len += 1
            l2 = l2.next
            
        # Determine if they are of different lengths
        diff = max(l1_len, l2_len) - min(l1_len, l2_len)
        
        if l1_len >= l2_len:
            l1, l2 = headA, headB
        else:
            l1, l2 = headB, headA
            
        # Traverse linked lists until intersection or end found
        while l1:
            if not diff:
                if l1 == l2:
                    return l1
                l1, l2 = l1.next, l2.next
            
            # Traverse longer linked list until remaining lengths are the same
            else:
                l1 = l1.next
                diff -= 1
                
        return None
