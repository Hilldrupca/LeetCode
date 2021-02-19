
// Provided by LeetCode
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

// Provided by LeetCode
impl ListNode {
  
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
        next: None,
        val
        }
    }

    fn path(self) -> Vec<i32> {
        // Returns the path values of the linked list.
        // Added to help with testing.
        let mut res: Vec<i32> = Vec::new();
        let mut node = Some(Box::new(self));
        
        while let Some(temp) = node {
            res.push(temp.val);
            node = temp.next;
        }
        
        res
    }
}

struct Solution {}

impl Solution {
    pub fn merge_two_lists(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Given two linked lists sorted in ascending order,
        // returns them merged in ascending order.
        // 
        // Constraints:
        //      The number of nodes in both lists is in the range [0, 50]
        //      -100 <= Node.val <= 100
        //      Both l1 and l2 are sorted in non-decreasing order
        
        let mut sentinel = Box::new(ListNode::new(0));
        
        let mut node = &mut sentinel.next;
        let mut one = l1;
        let mut two = l2;

        while one.is_some() && two.is_some() {
            let val1 = one.as_mut()?.val;
            let val2 = two.as_mut()?.val;

            if val1 < val2 {
                *node = Some(Box::new(ListNode::new(val1)));
                one = one?.next;
            } else {
                *node = Some(Box::new(ListNode::new(val2)));
                two = two?.next;
            }

            node = &mut node.as_mut().unwrap().next;
        }

        *node = match one.is_some() {
            true => one,
            false => two,
        };
        
        sentinel.next
    }
}

#[cfg(test)]
mod tests {
    
    use super::*;
    
    #[test]
    fn test_merge_two_lists() {
        // case one
        // l1 = 1 -> 2 -> 4     l2 = 1 -> 3 -> 4
        let l1 = Some(Box::new(ListNode{val: 1, next:
                    Some(Box::new(ListNode{val: 2, next:
                        Some(Box::new(ListNode::new(4)))}))}));
                        
        let l2 = Some(Box::new(ListNode{val: 1, next:
                    Some(Box::new(ListNode{val: 3, next:
                        Some(Box::new(ListNode::new(4)))}))}));
                      
        assert_eq!(
            match Solution::merge_two_lists(l1, l2) {
                Some(node) => node.path(),
                None => vec![],
            },
            vec![1,1,2,3,4,4],
        );
}
