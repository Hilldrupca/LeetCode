/// LeetCode Monthly Challenge problem for March 14th, 2021.
pub struct Solution {}

impl Solution {

    /// Swaps the values of the kth node from the front, and the kth node from
    /// the end. Returns the list unaltered if k is greater than the length, or
    /// if the kth elements are the same.
    ///
    /// # Arguments
    /// * head - The head node of a singely linked list.
    /// * k - The node from the front and back to swap values (1 indexed).
    ///
    /// # Example
    /// ```
    /// # use crate::swapping_nodes_linked_list::{ListNode, Solution};
    /// # let list = Some(Box::new(
    /// #     ListNode{
    /// #         val: 1,
    /// #         next: Some(Box::new(
    /// #             ListNode{
    /// #                 val: 2,
    /// #                 next: Some(Box::new(
    /// #                     ListNode{
    /// #                         val: 3,
    /// #                         next: Some(Box::new(
    /// #                             ListNode{
    /// #                                 val: 4,
    /// #                                 next: Some(Box::new(
    /// #                                     ListNode{
    /// #                                         val: 5,
    /// #                                         next: None
    /// #                                     }
    /// #                                 ))
    /// #                             }
    /// #                         ))
    /// #                     }
    /// #                 ))
    /// #             }
    /// #         ))
    /// #     }
    /// # ));
    /// // Given the following linked list:
    /// //
    /// //  1 -> 2 -> 3 -> 4 -> 5
    /// let ex = Solution::swap_nodes(list, 2);
    ///
    /// assert_eq!(
    ///     ListNode::values(ex),
    ///     vec![1,4,3,2,5]
    /// );
    /// ```
    ///
    /// # Constraints
    /// * The number of nodes in the list is n.
    /// * 1 <= k <= n <= 10^5
    /// * 0 <= node.val <= 100
    ///
    pub fn swap_nodes(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut head = head;

        let len = Solution::list_length(&head);
        
        if len - k + 1 == k || k > len { return head; }
        
        let front = k.min(len-k + 1);
        let end = k.max(len-k + 1);
        
        let mut first = &mut Box::new(ListNode::new(0));
        let mut second = head.as_mut().unwrap();
        
        let mut pos = 1;
        
        while pos != end {
            if pos == front {
                first = second;
                second = first.next.as_mut().unwrap();
            } else {
                second = second.next.as_mut().unwrap();
            }
            pos += 1
        }
        
        std::mem::swap(&mut first.val, &mut second.val);
        
        head
    }
    
    /// Returns the length of a singly linked list.
    fn list_length(node: &Option<Box<ListNode>>) -> i32 {
        match node {
            Some(n) => 1 + Solution::list_length(&n.next),
            None => 0,
        }
    }
}

/// ListNode struct provided By LeetCode.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {

    /// Creates a new ListNode. Provided by LeetCode.
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
    
    /// Returns the linked list's values in order. Used for testing
    /// Solution::swap_nodes()
    pub fn values(node: Option<Box<ListNode>>) -> Vec<i32> {
        let mut node = node.unwrap();
        let mut path = Vec::new();
        
        while node.next.is_some() {
            path.push(node.val);
            node = node.next.unwrap();
        }
        path.push(node.val);
        
        path
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn k_less_than_half_length() {
        let list = Some(Box::new(
            ListNode{
                val: 1,
                next: Some(Box::new(
                    ListNode{
                        val: 2,
                        next: Some(Box::new(
                            ListNode{
                                val: 3,
                                next: Some(Box::new(
                                    ListNode{
                                        val: 4,
                                        next: Some(Box::new(
                                            ListNode{
                                                val: 5,
                                                next: None
                                            }
                                        ))
                                    }
                                ))
                            }
                        ))
                    }
                ))
            }
        ));
        
        assert_eq!(
            ListNode::values(Solution::swap_nodes(list, 2)),
            vec![1,4,3,2,5]
        );
    }
    
    #[test]
    fn k_is_middle_element() {
        let list = Some(Box::new(
            ListNode{
                val: 1,
                next: Some(Box::new(
                    ListNode{
                        val: 2,
                        next: Some(Box::new(
                            ListNode{
                                val: 3,
                                next: Some(Box::new(
                                    ListNode{
                                        val: 4,
                                        next: Some(Box::new(
                                            ListNode{
                                                val: 5,
                                                next: None
                                            }
                                        ))
                                    }
                                ))
                            }
                        ))
                    }
                ))
            }
        ));
        
        assert_eq!(
            ListNode::values(Solution::swap_nodes(list, 3)),
            vec![1,2,3,4,5]
        );
    }
    
    #[test]
    fn k_greater_than_half_length() {
        let list = Some(Box::new(
            ListNode{
                val: 1,
                next: Some(Box::new(
                    ListNode{
                        val: 2,
                        next: Some(Box::new(
                            ListNode{
                                val: 3,
                                next: Some(Box::new(
                                    ListNode{
                                        val: 4,
                                        next: Some(Box::new(
                                            ListNode{
                                                val: 5,
                                                next: None
                                            }
                                        ))
                                    }
                                ))
                            }
                        ))
                    }
                ))
            }
        ));
        
        assert_eq!(
            ListNode::values(Solution::swap_nodes(list, 5)),
            vec![5,2,3,4,1]
        );
    }
    
    #[test]
    fn k_greater_than_length() {
        let list = Some(Box::new(
            ListNode{
                val: 1,
                next: Some(Box::new(
                    ListNode{
                        val: 2,
                        next: Some(Box::new(
                            ListNode{
                                val: 3,
                                next: Some(Box::new(
                                    ListNode{
                                        val: 4,
                                        next: Some(Box::new(
                                            ListNode{
                                                val: 5,
                                                next: None
                                            }
                                        ))
                                    }
                                ))
                            }
                        ))
                    }
                ))
            }
        ));
        
        assert_eq!(
            ListNode::values(Solution::swap_nodes(list, 6)),
            vec![1,2,3,4,5]
        );
    }
}
