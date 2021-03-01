use std::collections::HashSet;

pub struct Solution {}

/// LeetCode Monthly Challenge problem for March 1st, 2021.
impl Solution {

    /// Given a vector of i32 integers, returns the minimum of unique integers,
    /// or half the vector length.
    ///
    /// # Arguments
    ///
    /// * candy_type - A vector of i32 integers, each representing a type of
    /// candy.
    ///
    /// # Examples
    ///
    /// ```
    /// # use crate::distribute_candies::Solution;
    /// let ex_one = Solution::distribute_candies(vec![1,1,2,2,3,3]);
    /// let ex_two = Solution::distribute_candies(vec![1,1,2,3]);
    /// let ex_three = Solution::distribute_candies(vec![6,6,6,6]);
    ///
    /// assert_eq!(ex_one, 3);
    /// assert_eq!(ex_two, 2);
    /// assert_eq!(ex_three, 1);
    /// ```
    ///
    /// # Constraints
    ///
    /// * n == candy_type.len()
    /// * 2 <= n <= 10^4
    /// * n is even
    /// * -10^5 <= candy_type[i] <= 10^5
    ///
    pub fn distribute_candies(candy_type: Vec<i32>) -> i32 {
        let unique: HashSet<&i32> = candy_type.iter().collect();
        
        unique.len().min(candy_type.len()/2) as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn candy_unique_equals_half_length() {
        assert_eq!(
            Solution::distribute_candies(vec![1,1,2,2,3,3]),
            3,
        );
    }
    
    #[test]
    fn candy_half_length_greather_than_unique() {
        assert_eq!(
            Solution::distribute_candies(vec![1,1,2,3]),
            2
        );
    }
    
    #[test]
    fn candy_unique_less_than_half_length() {
        assert_eq!(
            Solution::distribute_candies(vec![6,6,6,6]),
            1,
        );
    }
}
