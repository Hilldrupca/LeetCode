
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
    def _path(self):
        '''Used for testing. Returns the path down a linked list'''
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
        
class Solution:
    '''
    LeetCode Challenge problem for November 2nd, 2020.
    '''
    def insertionSortList(self, head: ListNode) -> ListNode:
        '''
        In-place insertion sort of a linked list.
        
        Params:
            head - The head node of a linked list.
            
        Returns:
            ListNode - The head node of the sorted linked list.
            
        Examples:
            head = 4 -> 2 -> 1 -> 3
            insertionSortList(head)   ->   1   (1 -> 2 -> 3 -> 4)
            
            head = -1 -> 5 -> 3 -> 4 -> 0
            insertionSortList(head)   ->   -1   (-1 -> 0 -> 3 -> 4 -> 5)
        '''
        if not head or not head.next:
            return head
        
        dummy_head = ListNode(val=float('-inf'),next=head)
        node = dummy_head.next
        
        while node.next:
            if node.val > node.next.val:
                iter_node = dummy_head
                while iter_node.next.val < node.next.val:
                    iter_node = iter_node.next
                    
                n = node.next
                node.next = n.next
                iter_node.next, n.next = n, iter_node.next
            else:
                node = node.next
        
        return dummy_head.next
