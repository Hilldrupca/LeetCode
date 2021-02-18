
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        '''Provided by LeetCode.'''
        self.val = int(x)
        self.next = next
        self.random = random
        
    def _path(self):
        '''
        Used for testing.
        
        Returns the path of the linked list. Each element is the node's
        value, and the value of it's random node.
        '''
        res, node = [], self
        
        while node:
            rand = node.random.val if node.random else None
            res.append([node.val, rand])
            node = node.next
            
        return res
    

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 10th, 2021.
    '''
    def copyRandomList(self, head: Node) -> Node:
        '''
        Given a linked list where nodes also contain a random pointer, returns
        a deep copy.
        
        Constraints:
            0 <= n <= 1000
            -10000 <= node.val <= 10000
            node.random is None or is pointing to some node in the linked list
            
        Params:
            head - The head node of a linked list.
            
        Returns:
            Node - The head node of a deep copy of given linked list.
        '''
        old_to_new = {}
        sentinel = node = Node(x=0)
        
        while head:
            if head not in old_to_new:
                old_to_new[head] = Node(x=head.val)
                
            node.next = old_to_new[head]
            node = node.next
            
            if head.random:
                if head.random not in old_to_new:
                    old_to_new[head.random] = Node(x=head.random.val)
                
                node.random = old_to_new[head.random]
            
            head = head.next
            
        return sentinel.next
