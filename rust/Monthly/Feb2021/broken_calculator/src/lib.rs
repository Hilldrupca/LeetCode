
pub struct Solution {}

/// LeetCode Monthly Challenge problem for February 21st, 2021.
impl Solution {

    /// Given a starting number, x, and a target number, y, returns the number
    /// of allowed operations to reach y from x. The following operations are
    /// allowed at each step:
    ///
    /// * x may be multiplied by 2
    /// * x may have 1 subtracted from it
    ///
    /// # Arguments
    /// * x - The starting number.
    /// * y - The target number.
    ///
    /// # Examples
    /// ```
    /// # use crate::broken_calculator::Solution;
    /// let ex_one = Solution::broken_calc(2,3);
    /// let ex_two = Solution::broken_calc(5,8);
    /// let ex_three = Solution::broken_calc(3,10);
    /// let ex_four = Solution::broken_calc(1024,1);
    ///
    /// assert_eq!(ex_one, 2);
    /// assert_eq!(ex_two, 2);
    /// assert_eq!(ex_three, 3);
    /// assert_eq!(ex_four, 1023);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= x <= 10^9
    /// * 1 <= y <= 10^9
    pub fn broken_calc(x: i32, y: i32) -> i32 {
        
        let mut res: i32 = 0;
        let mut num = y;
        
        while num > x {
            res += 1 + num % 2;
            num += num % 2;
            num /= 2;
        }
        res + x - num
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_broken_calc() {
        assert_eq!(
            Solution::broken_calc(2,3),
            2,
        );
        
        assert_eq!(
            Solution::broken_calc(5,8),
            2,
        );
        
        assert_eq!(
            Solution::broken_calc(3,10),
            3,
        );
        
        assert_eq!(
            Solution::broken_calc(1024,1),
            1023,
        );
        
        assert_eq!(
            Solution::broken_calc(1,1000000000),
            39,
        );
        
        assert_eq!(
            Solution::broken_calc(68,71),
            34,
        );
    }
}
