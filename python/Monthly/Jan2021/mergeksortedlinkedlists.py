from collections import deque
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def _path(self):
        '''Used for testing. Returns path of linked list.'''
        res, node = [], self
        while node:
            res.append(node.val)
            node = node.next
            
        return res

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 24th, 2021
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        Given k linked lists sorted in ascendig order, merges them into one
        linked list sorted in ascending order.
        
        Constraints:
            k == len(lists)
            0 <= k <= 10**4
            0 <= len(lists[i]) <= 500
            -10**4 <= lists[i][j] <= 10**4
            lists[i] is sorted in ascending order
            Sum of len(lists[i]) wont exceed 10**4
            
        Params
            lists - A list of linked list head nodes. Each linked list should
                    be sorted in ascending order.
                    
        Returns:
            ListNode - The new head node after merging all linked lists sorted
                       in ascending order.
                       
        Example:
            Given the following linked lists a, b, and c:
            
                    a = 1 -> 4 -> 5
                    b = 1 -> 3 -> 4
                    c = 2 -> 6
                    
            mergeKLists([a,b,c])   ->   1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
        '''
        if not lists:
            return None
        
        queue = deque(lists)
        
        while len(queue) > 1:
            sentinel = node = ListNode()

            l1 = queue.popleft()
            l2 = queue.popleft()
            
            while l1 and l2:
                if l1.val < l2.val:
                    node.next, l1 = l1, l1.next
                else:
                    node.next, l2 = l2, l2.next
                    
                node = node.next
            
            if l1:
                node.next = l1
            else:
                node.next = l2
                
            queue.append(sentinel.next)
                
        return queue[0]
