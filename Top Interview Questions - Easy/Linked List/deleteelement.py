
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val
    
    def path(self):
        node = self
        res = [self.val]
        while node.next:
            node = node.next
            res.append(node.val)
            
        return res
    
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Delete from the end the nth element from a linked list, and
        return it's head.
        
        Params:
            head - The head element of a ListNode linked list.
            
            n - The nth element from the end to delete.
            
        Returns:
            ListNode - The head element of a linked list.
            
        Examples:
            rfe = removeNthFromEnd()
            Given the linked list [1,2,3,4,5,]:
                rfe(1, 4)   ->   1
                
                rfe(1, 5)   ->   2
                
            Given the linked list [1]
                rfe(1, 1)   ->   None
            
        '''
        linked = [head]
        
        while linked[-1].next:
            linked.append(linked[-1].next)
            
        size = len(linked)
        if n == size and size ==1:
            return
        elif n == size:
            return linked[1]
        elif n ==1:
            linked[-2].next = None
        else:
            linked[size-n-1].next = linked[size-n+1]
            
        return linked[0]
