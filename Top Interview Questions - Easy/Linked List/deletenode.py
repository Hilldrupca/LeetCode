
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def path(self):
        node = self
        res = [self.val]
        while node.next:
            node = node.next
            res.append(node.val)            
            
        return res
        
class Solution:
    def deleteNode(self, node):
        '''
        In-place deletion of a given node from a singly linked
        list (except the tail).
        
        Params:
            node - A node in a singly linked list.
            
        Returns:
            None - In-place deletion.
        '''
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
