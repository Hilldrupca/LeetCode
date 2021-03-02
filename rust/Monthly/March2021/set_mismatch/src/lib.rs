pub struct Solution {}

/// LeetCode Monthly Challenge problem for March 2nd, 2021.
impl Solution {

    /// Returns the duplicate number, and the number it replaced.
    /// 
    /// You have a set of integers s, which originally contains all the numbers
    /// from 1 to n. Unfortunately, due to some error, one of the numbers in s
    /// got duplicated to another number in the set, which results in
    /// repetition of one number and loss of another number.
    ///
    /// # Arguments
    /// * nums - A vector of integers from 1 to n with one duplicate, and one
    /// deletion.
    ///
    /// # Examples
    /// ```
    /// # use crate::set_mismatch::Solution;
    /// let ex_one = Solution::find_error_nums(vec![1,2,2,4]);
    /// let ex_two = Solution::find_error_nums(vec![1,1]);
    ///
    /// assert_eq!(ex_one, vec![2,3]);
    /// assert_eq!(ex_two, vec![1,2]);
    /// ```
    ///
    /// # Constraints
    /// * 2 <= nums.len() <= 10^4
    /// * 1 <= nums[i] <= 10^4
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![0,0];
        let mut total = 0;
        let mut seen = vec![false; nums.len() + 1];
        let m = nums.len() as i32;
        
        for n in nums {
            if seen[n as usize] {
                res[0] = n;
            } else {
                seen[n as usize] = true;
                total += n;
            }
        }
        
        res[1] = (m + 1) * m / 2 - total;
        
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn find_error_sorted_order() {
        assert_eq!(
            Solution::find_error_nums(vec![1,2,2,4]),
            vec![2,3],
        );
    }
    
    #[test]
    fn find_error_not_sorted() {
        assert_eq!(
            Solution::find_error_nums(vec![4,3,1,4,2]),
            vec![4,5],
        );
    }
    
    #[test]
    fn find_error_only_contains_dup() {
        assert_eq!(
            Solution::find_error_nums(vec![1,1]),
            vec![1,2],
        );
    }
}
