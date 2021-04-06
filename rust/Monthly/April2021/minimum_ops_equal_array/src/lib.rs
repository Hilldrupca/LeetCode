/// LeetCode Monthly Challenge problem for April 6th, 2021.
pub struct Solution {}

impl Solution {

    /// Given an array length n where arr[i] = 2 * i + 1, returns the minimum
    /// operations to make all elements equal.
    ///
    /// At each operation two indices are chosen, x and y. Then 1 is subtracted
    /// from arr[x], and 1 is added to arr[y].
    ///
    /// # Examples
    /// ```
    /// # use crate::minimum_ops_equal_array::Solution;
    /// let ex_one = Solution::min_operations(3);
    /// let ex_two = Solution::min_operations(6);
    ///
    /// assert_eq!(ex_one, 2);
    /// assert_eq!(ex_two, 9);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= n <= 10^4
    ///
    pub fn min_operations(n: i32) -> i32 {
        let mut res = 0;
        let (mut i, mut j) = (0, n - 1);
        
        while i < j {
            res += ((2 * j + 1) - (2 * i + 1)) / 2;
            i += 1;
            j -= 1;
        }
        
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_min_operations() {
        assert_eq!(
            Solution::min_operations(3),
            2
        );
        
        assert_eq!(
            Solution::min_operations(6),
            9
        );
        
        assert_eq!(
            Solution::min_operations(51),
            650
        );
        
        assert_eq!(
            Solution::min_operations(273),
            18632
        );
        
        assert_eq!(
            Solution::min_operations(10000),
            25000000
        );
    }
}
