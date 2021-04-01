/// LeetCode Monthly Challenge problem for April 1st, 2021.
pub struct Solution {}

impl Solution {

    /// Given the head node of a linked list, returns whether the nodes' values
    /// form are a palindrome.
    ///
    /// # Examples
    /// ```
    /// # use crate::palindrome_linked_list::{ListNode, Solution};
    /// # let ex_one = 
    /// #   Some(Box::new(ListNode{
    /// #       val: 1,
    /// #       next: Some(Box::new(ListNode{
    /// #           val: 2,
    /// #           next: Some(Box::new(ListNode{
    /// #               val: 2,
    /// #               next: Some(Box::new(ListNode{
    /// #                   val: 1,
    /// #                   next: None
    /// #               }))
    /// #           }))
    /// #       }))
    /// #   }));
    /// // ex_one = 1 -> 2 -> 2 -> 1
    /// assert_eq!(
    ///     Solution::is_palindrome(ex_one),
    ///     true
    /// );
    /// ```
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut node = head;
        let mut num = Vec::new();
        
        while let Some(n) = node {
            num.push(n.val);
            node = n.next;
        }
        
        let (mut i, mut j) = (0, num.len() - 1);
        
        while num[i] == num[j]  && i < j{
            i += 1;
            j -= 1;
        }
        
        num[i] == num[j]
    }
}

/// Linked list structure provided by LeetCode
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_is_palindrome() {
        let list = Some(
            Box::new(
                ListNode{
                    val: 1,
                    next: Some(
                        Box::new(
                            ListNode{
                                val: 2,
                                next: Some(
                                    Box::new(
                                        ListNode{
                                            val: 2,
                                            next: Some(
                                                Box::new(
                                                    ListNode{
                                                        val: 1,
                                                        next: None
                                                    }
                                                )
                                            )
                                        }
                                    )
                                )
                            }
                        )
                    )
                }
            )
        );
        
        assert_eq!(
            Solution::is_palindrome(list),
            true
        );
    }
    
    #[test]
    fn test_is_not_palindrome() {
        let list = Some(
            Box::new(
                ListNode{
                    val: 1,
                    next: Some(
                        Box::new(
                            ListNode{
                                val: 2,
                                next: None,
                            }
                        )
                    )
                }
            )
        );
        
        assert_eq!(
            Solution::is_palindrome(list),
            false,
        );
    }
}
