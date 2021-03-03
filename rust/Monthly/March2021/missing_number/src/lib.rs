pub struct Solution {}

/// LeetCode Monthly Challenge problem for March 3rd, 2021.
impl Solution {

    /// Given an array of distinct numbers in the range [0, n] that is missing
    /// one number, finds and returns the missing number.
    ///
    /// # Arguments
    /// * nums - A vector of distinct i32 integers in the range [0, n]
    ///
    /// # Examples
    /// ```
    /// # use crate::missing_number::Solution;
    /// let ex_one = Solution::missing_number(vec![3,0,1]);
    /// let ex_two = Solution::missing_number(vec![0,1]);
    /// let ex_three = Solution::missing_number(vec![9,6,4,2,3,5,7,0,1]);
    /// let ex_four = Solution::missing_number(vec![0]);
    ///
    /// assert_eq!(ex_one, 2);
    /// assert_eq!(ex_two, 2);
    /// assert_eq!(ex_three, 8);
    /// assert_eq!(ex_four, 1);
    /// ```
    ///
    /// # Constraints
    /// * n == nums.len()
    /// * 1 <= n <= 10^4
    /// * 0 <= nums[i] <= n
    /// * All the numbers of nums are unique
    ///
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let sum: i32 = nums.iter().sum();
        let n = nums.len();
        
        ((n + 1) * n / 2) as i32 - sum
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_missing_number() {
        assert_eq!(
            Solution::missing_number(vec![3,0,1]),
            2,
        );
        
        assert_eq!(
            Solution::missing_number(vec![0,1]),
            2,
        );
        
        assert_eq!(
            Solution::missing_number(vec![9,6,4,2,3,5,7,0,1]),
            8,
        );
        
        assert_eq!(
            Solution::missing_number(vec![0]),
            1,
        );
    }
}
