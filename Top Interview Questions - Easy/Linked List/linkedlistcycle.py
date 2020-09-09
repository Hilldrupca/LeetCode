
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next
        
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        Determine if a linked list contains a cycle.
        
        Params:
            head - The head of a linked list.
            
        Returns:
            bool - Whether or not the linked list contains a cycle.
            
        Exampels:
            **Assumed lists are linked list paths, and values are unique**
            hasCycle([3,2,0,4,2])   ->   True
            hasCycle([1,2,1])       ->   True
            hasCycle([1])           ->   False
        '''
        visited = set()
        node = head
        while node:
            if node in visited:
                return True
            
            visited.add(node)
            node = node.next
            
        return False
