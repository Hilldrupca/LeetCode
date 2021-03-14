use std::collections::HashMap;

/// LeetCode Monthly Challenge problem for March 13, 2021.
pub struct Solution {}

impl Solution {

    /// Given a vector of integers, returns the number of binary trees they can
    /// make mod 10^9 + 7.
    ///
    /// # Arguments
    /// * arr - A vector of i32 integers.
    ///
    /// # Examples
    /// ```
    /// # use crate::binary_trees_with_factors::Solution;
    /// let ex_one = Solution::num_factored_binary_trees(vec![2,4]);
    /// let ex_two = Solution::num_factored_binary_trees(vec![2,4,5,10]);
    /// let ex_three = Solution::num_factored_binary_trees(vec![2,5,10,20]);
    /// let ex_four = Solution::num_factored_binary_trees(vec![18,3,6,2]);
    ///
    /// assert_eq!(ex_one, 3);
    /// assert_eq!(ex_two, 7);
    /// assert_eq!(ex_three, 12);
    /// assert_eq!(ex_four, 12);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= arr.len() <= 1000
    /// * 2 <= arr[i] <= 10^9
    ///
    pub fn num_factored_binary_trees(arr: Vec<i32>) -> i32 {
        let mut arr = arr;
        arr.sort_unstable();
        
        let mut products = HashMap::new();
        let mut trees = 0;
        
        for i in 0..arr.len() {
            
            let mut combs = 1;
            
            for j in 0..i {
                
                if arr[i] % arr[j] == 0 {
                    let seek = arr[i] / arr[j];
                    
                    match (products.get(&arr[j]), products.get(&seek)) {
                        (Some(a), Some(b)) => combs += a * b,
                        (_, _) => (),
                    
                    };
                }
            }
            
            trees += combs;
            products.insert(arr[i], combs);
            
        }
        
        (trees % (10_usize.pow(9) + 7)) as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn binary_trees_sorted_nums() {
        assert_eq!(
            Solution::num_factored_binary_trees(vec![2,4]),
            3
        );
        
        assert_eq!(
            Solution::num_factored_binary_trees(vec![2,4,5,10]),
            7
        );
        
        assert_eq!(
            Solution::num_factored_binary_trees(vec![2,5,10,20]),
            12
        );
    }
    
    #[test]
    fn binary_trees_unsorted_nums() {
        assert_eq!(
            Solution::num_factored_binary_trees(vec![18,3,6,2]),
            12
        );
    }
}
