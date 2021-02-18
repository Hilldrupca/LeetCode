
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def _path(self):
        '''Helper function. Used to confirm correct path.'''
        
        res, node = [], self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 4th, 2021.
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Given two sorted linked lists, returns a sorted merged list.
        
        Constraints:
            The number of nodes in both lists is in the range [0, 50]
            -100 <= Node.val <= 100
            Both l1 and l2 are sorted in non-decreasing order
        
        Params:
            l1 - The head node of a linked list
            
            l2 - The head node of another linked lists.
            
        Returns:
            ListNode - The head node of the merged linked lists sorted in
                       non-decreasing order.
                       
        Examples:
            ## Assume lists are linked lists ##
            mergeTwoLists([1,2,4], [1,3,4])   ->   [1,1,2,3,4,4]
            mergeTwoLists([], [1])            ->   [1]
            mergeTwoLists([], [])             ->   []
        '''
        sentinel = node = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
                
            node = node.next
            
        if not l1:
            node.next = l2
        elif not l2:
            node.next = l1
            
        return sentinel.next
