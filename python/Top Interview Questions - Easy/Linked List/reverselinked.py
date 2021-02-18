
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def path(self):
        node = self
        res = [self.val]
        while node.next:
            node = node.next
            res.append(node.val)            
            
        return res
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        Reverses a singly linked list.
        
        Params:
            head - The head of a singly linked list of ListNodes.
            
        Returns:
            Listnode - The new head of the reversed linked list, or None
                       if the original head == None.
                       
        Example:
            # List represenation of ListNode path [1,2,3,4,5]
            reverseList(1)   ->   new head = 5, head.path() = [5,4,3,2,1]
        '''
        if not head or not head.next:
            return head
        
        prev, node = None, head
        while node.next:
            node.next, node, prev = prev, node.next, node
            
        node.next = prev
        return node
