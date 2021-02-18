from typing import Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def _path(self):
        '''Helper method to ensure correct next values'''
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
            
        return res
    
class Solution:
    '''
    LeetCode Monthly Challenge for October 13th, 2020.
    '''
    def sortList(self, head: ListNode) -> ListNode:
        '''
        Returns the head node of a linked list after sorting. Uses merge sort,
        and attempts to us O(1) memory. Recursive merge sort is commented out
        at the end.
        
        Params:
            head - The head node of a linked list.
            
        Returns:
            ListNode - The (new) head node of the sorted linked list.
            
        Example:
            Given the following linked list:
                
                4 -> 2 -> 1 -> 3
                
            sortList(4)   ->   1 whose path = 1 -> 2 -> 3 -> 4
        '''
        if not head or not head.next:
            return head
        
        length = self._get_length(head)
        gap = 1
        while gap < length:
            start1 = head
            first_iter = True
            while start1:

                end1 = self._end_point(start1, gap)
                
                # Break in case the first segment is the end of the linked list
                start2 = end1.next
                if not start2:
                    break

                end2 = self._end_point(start2, gap)
                
                # Store starting point of next iteration
                temp = end2.next
                start1, end2 = self._merge(start1, end1, start2, end2)
                
                # Piece sorted segments together
                if first_iter:
                    head = start1
                    first_iter = False
                else:
                    prev.next = start1

                prev = end2
                start1 = temp
            
            # Ensures tail ListNode's next = None
            prev.next = start1
            gap *= 2

        return head
        
    def _merge(self, start1: ListNode, end1: ListNode,
              start2: ListNode, end2: ListNode) -> Tuple[ListNode, ListNode]:
        '''
        Merges and sorts two linked list segments
        
        Params:
            start1 - The starting ListNode of first linked list segment.
            
            end1 - The ending ListNode of first linked list segment.
            
            start2 - The starting ListNode of second linked list segment.
            
            end2 - The ending ListNode of second linked list segment.
            
        Returns:
            Tuple[ListNode, ListNode] - Returns both the (new) head ListNode,
                                        and the (new) tail ListNode of the
                                        current segment.
            
        '''

        if start1.val > start2.val:
            start1, start2 = start2, start1
            end1, end2 = end2, end1

        head = start1
        stop2 = end2.next

        while start1 != end1 and start2 != stop2:
            if start1.next.val > start2.val:
                start1.next, start2.next, start2 = start2, start1.next, \
                                                   start2.next

            start1 = start1.next

        if start1 == end1:
            start1.next = start2
        else:
            end2 = end1

        return head, end2

    def _end_point(self, node, gap) -> ListNode:
        '''
        Returns the ListNode at the end of the current gap distance.
        
        Params:
            node - The ListNode to start from.
            
            gap - The number of nodes to include in the segment.
           
        Returns:
            ListNode - The ListNode at the end of the gap.
        '''
        
        while gap > 1 and node.next:
            gap -= 1
            node = node.next

        return node

    def _get_length(self, node) -> int:
        '''Returns the length of the linked list'''
        
        length = 0
        while node:
            length += 1
            node = node.next

        return length
        
        
        
        
        
'''
### NOTE: Below is a recursive version of merge sort.
        
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def middle(node: ListNode) -> ListNode:
            slow = fast = node
            while fast.next and fast.next.next:
                slow, fast = slow.next, fast.next.next
                
            return slow
        
        def sorted_merge(left: ListNode, right: ListNode) -> ListNode:
            if left == None:
                return right
            
            elif right == None:
                return left
            
            elif left.val <= right.val:
                left.next = sorted_merge(left.next, right)
                return left
            
            else:
                right.next = sorted_merge(left, right.next)
                return right
        
        def merge_sort(node: ListNode) -> ListNode:
            if not node or not node.next:
                return node
            
            slow = fast = node
            while fast.next and fast.next.next:
                slow, fast = slow.next, fast.next.next

            next_to_mid = slow.next
            slow.next = None
            
            return sorted_merge(merge_sort(node), merge_sort(next_to_mid))
        
        
        if not head or not head.next:
            return head
        
        return merge_sort(head)
'''
