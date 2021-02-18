from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def path(self) -> List[int]:
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Returns a new linked list with corresponding nodes in l1 and l2 added
        together. Numbers represented by l1 and l2 should be in reversed order.
        Meaning the least significant digit should be the head nodes.
        
        Params:
            l1, l2 - Non-empty linked lists of non-negative integers. No
                     leading zeroes except for 0 itself. Each node should
                     represent a single digit.
                     
        Returns:
            ListNode - The head node of a singly linked list. Represented
                       number is also in reverse order.
            
        Examples:
            ***Assume lists are linked lists***
            addTwoNumbers([2,4,3],[5,6,4])   ->   [7,0,8]
            addTwoNumbers([5],[5])           ->   [0,1]
            addTwoNumbers([1,8],[0])         ->   [1,8]
        '''
        node_one = l1
        node_two = l2
        ll_sum = new_ll = ListNode()
        while node_one or node_two:
            # Add values if nodes exist
            if node_one:
                ll_sum.val += node_one.val
                node_one = node_one.next
            if node_two:
                ll_sum.val += node_two.val
                node_two = node_two.next

            # Numbers greater than 9 have a carryover of 1
            rem = 0
            if ll_sum.val > 9:
                ll_sum.val -= 10
                rem = 1
            
            if node_one or node_two or rem:
                ll_sum.next = ListNode(val=rem)
                ll_sum = ll_sum.next
            
        return new_ll
