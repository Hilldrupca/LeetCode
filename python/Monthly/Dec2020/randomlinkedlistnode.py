from random import randint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 2nd, 2020.
    '''
    def __init__(self, head: ListNode):
        '''
        Given a linked list, finds its size to help with random selection.
        '''
        if type(head) != ListNode:
            raise ValueError(
                f'Head node must be of type ListNode, got {type(head)}')
        
        self.head = node = head
        self.size = 1
        
        while node.next:
            node = node.next
            self.size += 1
            
    def getRandom(self) -> int:
        '''
        Returns a random node value from the linked list.
        '''
        idx, goal = 1, randint(1, self.size)
        node = self.head
        while idx < goal:
            node = node.next
            idx += 1
            
        return node.val
