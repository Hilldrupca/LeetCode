
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next
        
    def path(self):
        node = self
        res = [self.val]
        while node.next:
            node = node.next
            res.append(node.val)            
            
        return res
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Merge two linked lists and return as a new sorted linked list.
        
        Params:
            l1, l2 - The head nodes of two linked lists
            
        Returns:
            ListNode - Head node of the newly merged and sorted linked list.
            
        Examples:
            **Lists are used to show the paths starting from ListNode heads.**
            
            mergeTwoLists([1,2,4], [1,3,4])   ->   [1,1,2,3,4,4]
            mergeTwoLists([], [1,3,4])        ->   [1,3,4]
            mergeTwoLists([1,2,4], [])        ->   [1,2,4]
            mergeTwoLists([], [])             ->   []
        '''
        if not l1:
            return l2
        if not l2:
            return l1
        
        node_list = [l1]
        while node_list[-1].next:
            node_list.append(node_list[-1].next)
            
        node_list.append(l2)
        while node_list[-1].next:
            node_list.append(node_list[-1].next)
            
        node_list = sorted(node_list, key=lambda x: x.val)
        
        for x in range(len(node_list)-1):
            node_list[x].next = node_list[x+1]
            
        node_list[-1].next = None
        return node_list[0]
