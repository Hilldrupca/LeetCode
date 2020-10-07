
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def _path(self):
        '''Returns the linked list path in list form. Used for testing'''
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
        
class Solution:
    '''
    LeetCode Monthly Challenge for October 7th, 2020.
    '''
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        Returns the new head node of a linked list after rotating it k places
        to the right.
        
        Params:
            head - The head node of a linked list.
            
            k - The number of right shifts to perform.
            
        Returns:
            ListNode - The new head linked list node after shifting right k
                       times.
                       
        Examples:
            ***Assume lists are linked lists***
            rotateRight([1,2,3,4,5], 2)   ->   [4,5,1,2,3]
            rotateRight([0,1,2], 4)       ->   [2,0,1]
            rotateRight([1,2], 1)         ->   [2,1]
        '''
        if not head:
            return head
        
        length = 0
        node = tail = head
        while node:
            tail, node = node, node.next
            length += 1
            
        k = k % length
        
        if not k:
            return head
        
        node = prev = tail.next = head
        while length > k:
            length -= 1
            prev, node = node, node.next
            
        prev.next = None            
        
        return node
