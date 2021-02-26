pub struct Solution {}

/// LeetCode Monthly Challenge problem for February 26th, 2021.
impl Solution {
    
    /// Given two sequences pushed and popped with distinct values, return true if
    /// and only if this could have been the result of a sequence of push and pop
    /// operations on an initially empty stack.
    
    /// # Arguments
    /// * pushed - A vector of integers pushed onto an initially empty stack.
    /// * popped - A possible pop sequence of pushed..
    
    /// # Examples
    /// ```
    /// # use crate::valid_stack_sequence::Solution;
    /// let ex_one = Solution::validate_stack_sequences(
    ///     vec![1,2,3,4,5], vec![4,5,3,2,1],
    /// );
    /// let ex_two = Solution::validate_stack_sequences(
    ///     vec![1,2,3,4,5], vec![4,3,5,1,2],
    /// );
    ///
    /// assert_eq!(ex_one, true);
    /// assert_eq!(ex_two, false);
    /// ```
    
    /// # constraints
    /// * 0 <= pushed.len() == popped.len() <= 1000
    /// * 0 <= pushed[i], popped[i] < 1000
    /// * pushed is a permutation of popped
    /// * pushed and popped have distinct values
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut pop_iter = popped.iter();
        let mut stack = Vec::new();
        
        let mut next = pop_iter.next();
        
        for n in pushed.iter() {
            stack.push(*n);
            
            while !stack.is_empty() && stack.last() == next {
                stack.pop();
                next = pop_iter.next();
            }
        }
        
        stack.is_empty() && next == None
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn valid_sequences() {
        assert!(
            Solution::validate_stack_sequences(
                vec![1,2,3,4,5],
                vec![4,5,3,2,1]
            )
        );
    }
    
    #[test]
    fn invalid_sequences() {
        assert_eq!(
            Solution::validate_stack_sequences(
                vec![1,2,3,4,5],
                vec![4,3,5,1,2]
            ),
            false
        );
    }
}
