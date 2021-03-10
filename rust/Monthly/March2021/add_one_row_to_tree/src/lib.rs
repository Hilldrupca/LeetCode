use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

/// Tree structure provided by LeetCode
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    
    /// Creates a new TreeNode. Provided by LeetCode.
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode{
            val,
            left: None,
            right: None
        }
    }
}

/// LeetCode Monthly Challenge problem for March 9th, 2021.
pub struct Solution {}

impl Solution {

    /// Given the root of a binary tree, then value v and depth d, you need to
    /// add a row of nodes with value v at the given depth d. The root node is
    /// at depth 1.

    /// The adding rule is: given a positive integer depth d, for each NOT null
    /// tree nodes N in depth d-1, create two tree nodes with value v as N's
    /// left subtree root and right subtree root. And N's original left subtree
    /// should be the left subtree of the new left subtree root, its original
    /// right subtree should be the right subtree of the new right subtree root.
    /// If depth d is 1 that means there is no depth d-1 at all, then create a
    /// tree node with value v as the new root of the whole original tree, and
    /// the original tree is the new root's left subtree.
    ///
    /// # Arguments
    /// * root - The root node of a binary tree.
    /// * v - The value of newly inserted nodes.
    /// * d - The level of the binary tree to insert the row (1 indexed).
    ///
    /// # Example
    /// ```
    /// # use crate::add_one_row_to_tree::{Solution, TreeNode};
    /// # use std::rc::Rc;
    /// # use std::cell::RefCell;
    /// # let root = Some(Rc::new(RefCell::new(
    /// #   TreeNode{
    /// #       val: 4,
    /// #       left: Some(Rc::new(RefCell::new(
    /// #           TreeNode{
    /// #               val: 2,
    /// #               left: Some(Rc::new(RefCell::new(TreeNode::new(3)))),
    /// #               right: Some(Rc::new(RefCell::new(TreeNode::new(1)))),
    /// #           }
    /// #       ))),
    /// #       right: Some(Rc::new(RefCell::new(
    /// #           TreeNode{
    /// #               val: 6,
    /// #               left: Some(Rc::new(RefCell::new(TreeNode::new(5)))),
    /// #               right: None
    /// #           }
    /// #       )))
    /// #   }
    /// # )));
    /// // Given the following binary tree before and after insertion:
    /// //      __4__                 __4__
    /// //     /     \               /     \
    /// //    2       6     =>      1       1
    /// //   / \     /             /         \
    /// //  3   1   5             2           6
    /// //                       / \         /
    /// //                      3   1       5
    /// let ex_one = Solution::add_one_row(root, 1, 2);
    ///
    /// assert_eq!(
    ///     Solution::level_order(ex_one),
    ///     vec![Some(4),
    ///          Some(1), Some(1),
    ///          Some(2), None, None, Some(6),
    ///          Some(3), Some(1), Some(5), None,
    ///          None, None, None, None, None, None
    ///     ]
    /// );
    /// ```
    ///
    /// # Constraints
    /// * The given d is in range [1, max depth of given tree + 1]
    /// * The binary tree has at least one node.
    ///
    pub fn add_one_row(root: Option<Rc<RefCell<TreeNode>>>, v: i32, d: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if d == 1 {
            let mut new_root = TreeNode::new(v);
            new_root.left = root;
            return Some(Rc::new(RefCell::new(new_root)))
        }
        
        Solution::recursive_add_row(
            root.as_ref().unwrap().clone(),
            2,
            v,
            d
        );
        
        root
    }
    
    fn recursive_add_row(node: Rc<RefCell<TreeNode>>, level: i32, v: i32, d: i32) {
        if level != d {
            
            if let Some(left) = &node.borrow().left { 
                Solution::recursive_add_row(
                    left.clone(),
                    level + 1,
                    v,
                    d
                );
            }
            
            if let Some(right) = &node.borrow().right {
                Solution::recursive_add_row(
                    right.clone(),
                    level + 1,
                    v,
                    d
                );
            }
            
        } else {
            let mut n = node.borrow_mut();
            
            n.left = Some(
                Rc::new(
                    RefCell::new(
                        TreeNode{
                            val: v,
                            left: n.left.take(),
                            right: None
                        }
                    )
                )
            );
            
            n.right = Some(
                Rc::new(
                    RefCell::new(
                        TreeNode{
                            val: v,
                            left: None,
                            right: n.right.take()
                        }
                    )
                )
            )
        }
    }
    
    /// Returns the level order traversal of a binary tree.
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Option<i32>> {
        let mut order: Vec<Option<i32>> = Vec::new();
        let mut nodes: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();
        nodes.push_front(root);
        
        while let Some(node) = nodes.pop_front() {
            
            if let Some(n) = node {
                order.push(Some(n.borrow().val));
                nodes.push_back(n.borrow_mut().left.take());
                nodes.push_back(n.borrow_mut().right.take());
            } else {
                order.push(None);
            }
        }
        
        order
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn mixed_trees() {
        //      __4__                 __4__
        //     /     \               /     \
        //    2       6     =>      1       1
        //   / \     /             /         \
        //  3   1   5             2           6
        //                       / \         /
        //                      3   1       5
        let root = Some(Rc::new(RefCell::new(
            TreeNode{
                val: 4,
                left: Some(Rc::new(RefCell::new(
                    TreeNode{
                        val: 2,
                        left: Some(Rc::new(RefCell::new(TreeNode::new(3)))),
                        right: Some(Rc::new(RefCell::new(TreeNode::new(1)))),
                    }
                ))),
                right: Some(Rc::new(RefCell::new(
                    TreeNode{
                        val: 6,
                        left: Some(Rc::new(RefCell::new(TreeNode::new(5)))),
                        right: None
                    }
                )))
            }
        )));
        
        assert_eq!(
            Solution::level_order(Solution::add_one_row(root, 1, 2)),
            vec![Some(4),
                 Some(1), Some(1),
                 Some(2), None, None, Some(6),
                 Some(3), Some(1), Some(5), None,
                 None, None, None, None, None, None
            ]
        );
        
        //      4                   4
        //     /                   / 
        //    2         =>        2
        //   / \                 / \
        //  3   1               1   1
        //                     /     \
        //                    3       1
        let root = Some(Rc::new(RefCell::new(
            TreeNode{
                val: 4,
                left: Some(Rc::new(RefCell::new(
                    TreeNode{
                        val: 2,
                        left: Some(Rc::new(RefCell::new(TreeNode::new(3)))),
                        right: Some(Rc::new(RefCell::new(TreeNode::new(1))))
                    }
                ))),
                right: None
            }
        )));
        
        assert_eq!(
            Solution::level_order(Solution::add_one_row(root, 1, 3)),
            vec![Some(4),
                 Some(2), None,
                 Some(1), Some(1),
                 Some(3), None, None, Some(1),
                 None, None, None, None
            ]
        );
    }
    
    #[test]
    fn single_node_tree() {
        //                      1
        //      4       =>     / 
        //                    4
        let root = Some(Rc::new(RefCell::new(TreeNode::new(4))));
        
        assert_eq!(
            Solution::level_order(Solution::add_one_row(root, 1, 1)),
            vec![Some(1),
                 Some(4), None,
                 None, None
            ]
        );
    }
    
    #[test]
    fn add_row_at_max_depth() {
        //                      4
        //      4       =>     / \
        //                    1   1
        let root = Some(Rc::new(RefCell::new(TreeNode::new(4))));
        
        assert_eq!(
            Solution::level_order(Solution::add_one_row(root, 1, 2)),
            vec![Some(4),
                 Some(1), Some(1),
                 None, None, None, None
            ]
        );
    }
}
