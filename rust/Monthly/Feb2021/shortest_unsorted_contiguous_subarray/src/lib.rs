pub struct Solution {}

/// LeetCode Monthly Challenge problem for February 25th, 2021.
impl Solution {

    // Same as Python's bisect module
    fn bisect_left(nums: &Vec<i32>, mut l: usize, mut r: usize, t: &i32) -> usize {
        while l < r {
            let m = (l + r) / 2;
            if nums[m] < *t { l = m + 1; } else { r = m; }
        }
        
        l
    }
    
    /// Same as Python's bisect module
    fn bisect_right(nums: &Vec<i32>, mut l: usize, mut r: usize, t: &i32) -> usize{
        while l < r {
            let m = (l + r) / 2;
            if nums[m] > *t { r = m; } else { l = m + 1; }
        }
        
        l
    }
    
    /// Returns the length of the continuous subarray that if sorted makes the
    /// entire vector sorted.
    ///
    /// # Arguments
    /// * nums - A vector of i32 integers.
    ///
    /// # Examples:
    /// ```
    /// # use crate::shortest_unsorted_contiguous_subarray::Solution;
    /// let ex_one = Solution::find_unsorted_subarray(vec![2,6,4,8,10,9,15]);
    /// let ex_two = Solution::find_unsorted_subarray(vec![1,2,3,4]);
    /// let ex_three = Solution::find_unsorted_subarray(vec![1]);
    /// let ex_four = Solution::find_unsorted_subarray(vec![1,3,2,2,2]);
    ///
    /// assert_eq!(ex_one, 5);
    /// assert_eq!(ex_two, 0);
    /// assert_eq!(ex_three, 0);
    /// assert_eq!(ex_four, 4);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= nums.len() <= 10^4
    /// * -10^5 <= nums[i] <= 10^5
    ///
    pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {

        let mut i = 0;
        while i < nums.len() - 1 && nums[i] <= nums[i+1]{ i += 1; }
        
        if i == nums.len() - 1 { return 0; }
        
        let mut j = nums.len() - 1;
        while j > 0 && nums[j] >= nums[j-1] { j -= 1; }
        
        let l = Solution::bisect_right(
            &nums,
            0,
            i,
            nums[i..j+1].iter().min().unwrap(),
        );
        
        let r = Solution::bisect_left(
            &nums,
            j,
            nums.len(),
            nums[i..j+1].iter().max().unwrap(),
        );
        
        (r - l) as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_unsorted_subarray() {
        assert_eq!(
            Solution::find_unsorted_subarray(vec![2,6,4,8,10,9,15]),
            5,
        );
        
        assert_eq!(
            Solution::find_unsorted_subarray(vec![1,2,3,4]),
            0,
        );
        
        assert_eq!(
            Solution::find_unsorted_subarray(vec![1]),
            0,
        );
        
        assert_eq!(
            Solution::find_unsorted_subarray(vec![1,3,2,2,2]),
            4,
        );
        
        assert_eq!(
            Solution::find_unsorted_subarray(vec![3,3,1,2,2]),
            5,
        );
        
        assert_eq!(
            Solution::find_unsorted_subarray(vec![1,3,2,3,3]),
            2,
        );
        
        assert_eq!(
            Solution::find_unsorted_subarray(vec![1,2,3,4,5,5,4,3,2,1,1,2,3,4,5]),
            13,
        );
    }
}
