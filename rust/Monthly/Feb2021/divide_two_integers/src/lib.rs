pub struct Solution {}

/// LeetCode Monthly Challenge problem for February 27th, 2021.
impl Solution {

    /// Divides two integers without using multiplication, division, or mod
    /// operators. If division results in overflow, then std::i32::MAX is
    /// returned.
    
    /// # Arguments
    /// * dividend - The number to be divided.
    /// * divisor - The number to divide dividend by.
    
    /// # Exmples
    /// ```
    /// # use crate::divide_two_integers::Solution;
    /// let ex_one = Solution::divide(10, 3);
    /// let ex_two = Solution::divide(7, -3);
    /// let ex_three = Solution::divide(std::i32::MIN, -1);
    ///
    /// assert_eq!(ex_one, 3);
    /// assert_eq!(ex_two, -2);
    /// assert_eq!(ex_three, std::i32::MAX);
    /// ```
    
    /// # Constraints
    /// * -2^31 <= dividend, divisor <= 2^31 - 1
    /// * divisor != 0
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        let n = match dividend {
            i if i < 0 => !dividend as u32 + 1,
            _ => dividend as u32,
        };
        
        let d = match divisor {
            i if i < 0 => !divisor as u32 + 1,
            _ => divisor as u32,
        };
        
        let mut r = 0;                     // remainder
        let mut q = 0;                     // quotient
        let mut m = n.next_power_of_two(); // dividend bit tracker
        
        while m > 0 {
            r <<= 1;
            if n & m == m { r += 1; }
            q <<= 1;
            
            if r >= d {
                r -= d;
                q += 1;
            }
            
            m >>= 1;
        }
        
        if dividend.signum() + divisor.signum() == 0  && q != 0{
            (!q + 1) as i32
        } else if q >= 2u32.pow(31) - 1 {
            std::i32::MAX
        } else {
            q as i32
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn divide_pos_pos() {
        assert_eq!(
            Solution::divide(10, 3),
            3,
        );
    }
    
    #[test]
    fn divide_pos_neg() {
        assert_eq!(
            Solution::divide(7, -3),
            -2,
        );
    }
    
    #[test]
    fn divide_neg_neg() {
        assert_eq!(
            Solution::divide(-6, -4),
            1,
        );
    }
    
    #[test]
    fn divide_i32min_neg_one() {
        assert_eq!(
            Solution::divide(std::i32::MIN, -1),
            std::i32::MAX,
        );
    }
    
    #[test]
    fn divide_extras() {
        assert_eq!(
            Solution::divide(0, 1),
            0,
        );
        
        assert_eq!(
            Solution::divide(1,1),
            1,
        );
        
        assert_eq!(
            Solution::divide(std::i32::MIN, 1),
            std::i32::MIN,
        );
        
        assert_eq!(
            Solution::divide(std::i32::MIN, 2),
            -1073741824,
        );
        
        assert_eq!(
            Solution::divide(std::i32::MAX, std::i32::MIN),
            0,
        );
    }
}
