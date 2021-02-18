from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def order_check(self) -> List[int]:
        '''
        Traverse and create path of linked list.
        
        Returns:
            list - order of linked lists' node val properties
        '''
        
        # Naive cycle check assumes self.val is unique
        visited = set()
        visited.add(self.val)
        path = [self.val]
        node = self
        while node.next:
            node = node.next
            if node.val not in visited:
                visited.add(node.val)
                path.append(node.val)
            else:
                raise RuntimeError(f'Cycle detected! {path} -> {node.val}')
               
        return path
    
class Solution:
    '''
    LeetCode Monthly Challenge problem for August 20th, 2020.
    '''
    def reorderList(self, head: ListNode) -> None:
        '''
        In place reorder of linked list.
        
        Given a singly linked list L: L0 -> L1 -> ... -> Ln-1 -> Ln,
        reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
        
        Params:
            head - beginning node of a linked list.
            
        Returns:
            None
        '''
        from collections import deque
        
        if not isinstance(head, ListNode):
            return
        
        head_list = deque([head])
        
        # Visited every node in the linked list and add to deque
        while head_list[-1].next:
            next_node = head_list[-1].next
            head_list.append(next_node)
        
        # Alternate linking front of deque with end
        prev = None
        while len(head_list):
            front = head_list.popleft()
            if prev:
                prev.next = front
                
            if len(head_list):
                front.next = prev = head_list.pop()
            else:
                front.next = prev = None
        
        # If linked list length is even, set .next of last item to None
        if prev:
            prev.next = None
            
