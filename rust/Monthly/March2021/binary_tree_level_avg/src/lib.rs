use std::rc::Rc;
use std::cell::RefCell;

/// Binary tree data structure provided by LeetCode.
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {

    /// Creates a new TreeNode. Provided by LeetCode
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub struct Solution {}

/// LeetCode Monthly Challenge problem for March 5th, 2021.
impl Solution {

    /// Returns the average values of each level of a binary tree. Returns an
    /// empty vector if the root is None.
    ///
    /// # Arguments
    /// * root - The root node of a binary tree.
    ///
    /// # Example
    /// ```
    /// # use crate::binary_tree_level_avg::{Solution, TreeNode};
    /// # use std::rc::Rc;
    /// # use std::cell::RefCell;
    /// #
    /// # let node_fifteen = TreeNode::new(15);
    /// # let node_seven = TreeNode::new(7);
    /// # let mut node_twenty = TreeNode::new(20);
    /// # node_twenty.left = Some(Rc::new(RefCell::new(node_fifteen)));
    /// # node_twenty.right = Some(Rc::new(RefCell::new(node_seven)));
    /// # let node_nine = TreeNode::new(9);
    /// # let mut node_three = TreeNode::new(3);
    /// # node_three.left = Some(Rc::new(RefCell::new(node_nine)));
    /// # node_three.right = Some(Rc::new(RefCell::new(node_twenty)));
    /// # let root = Some(Rc::new(RefCell::new(node_three)));
    /// // Given the following binary tree:
    /// //
    /// //      3
    /// //     / \
    /// //    9   20
    /// //       /  \
    /// //      15   7
    /// //
    /// let ex = Solution::average_of_levels(root);
    ///
    /// assert_eq!(ex, vec![3.0, 14.5, 11.0]);
    /// ```
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        
        let mut res: Vec<f64> = Vec::new();
        let mut current_level: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        let mut next_level: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        let mut size = 0;
        let mut level_sum: f64 = 0.0;
        
        if let Some(node) = root { current_level.push(node); }
        
        while let Some(node) = current_level.pop() {
            
            level_sum += node.borrow().val as f64;
            size += 1;
            
            if let Some(left) = &node.borrow().left {
                next_level.push(left.clone());
            }
            
            if let Some(right) = &node.borrow().right { 
                next_level.push(right.clone());
            }
            
            if current_level.is_empty() {
                current_level.append(&mut next_level);
                res.push(level_sum / size as f64);
                level_sum = 0.0;
                size = 0;
            }
        }
        
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn populated_tree() {
        // binary tree:
        //
        //      3
        //     / \
        //    9   20
        //       /  \
        //      15   7
        //
        
        let node_fifteen = TreeNode::new(15);
        let node_seven = TreeNode::new(7);
        
        let mut node_twenty = TreeNode::new(20);
        node_twenty.left = Some(Rc::new(RefCell::new(node_fifteen)));
        node_twenty.right = Some(Rc::new(RefCell::new(node_seven)));
        
        let node_nine = TreeNode::new(9);
        
        let mut node_three = TreeNode::new(3);
        node_three.left = Some(Rc::new(RefCell::new(node_nine)));
        node_three.right = Some(Rc::new(RefCell::new(node_twenty)));
        
        let root = Some(Rc::new(RefCell::new(node_three)));
        
        assert_eq!(
            Solution::average_of_levels(root),
            vec![3.0, 14.5, 11.0],
        );
    }
    
    #[test]
    fn empty_tree() {
        assert_eq!(
            Solution::average_of_levels(None),
            vec![],
        );
    }
}
