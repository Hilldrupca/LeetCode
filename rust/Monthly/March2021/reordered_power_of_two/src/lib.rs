/// LeetCode Monthly Challenge problem for March 21st, 2021.
pub struct Solution {}

impl Solution {

    /// Returns whether or not a given number could be rearranged to a power
    /// of 2 (excluding rearrangements with leading zeroes).
    ///
    /// # Arguments
    /// * n - An i32 integer greater than 0.
    ///
    /// # Examples
    /// ```
    /// # use crate::reordered_power_of_two::Solution;
    /// let ex_one = Solution::reordered_power_of2(1);
    /// let ex_two = Solution::reordered_power_of2(10);
    /// let ex_three = Solution::reordered_power_of2(16);
    /// let ex_four = Solution::reordered_power_of2(24);
    /// let ex_five = Solution::reordered_power_of2(46);
    ///
    /// assert_eq!(ex_one, true);
    /// assert_eq!(ex_two, false);
    /// assert_eq!(ex_three, true);
    /// assert_eq!(ex_four, false);
    /// assert_eq!(ex_five, true);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= n <= 10^9
    ///
    pub fn reordered_power_of2(n: i32) -> bool {
        let n_counts = Solution::digit_counts(n);
        let min = Solution::n_min(&n_counts);
        let max = Solution::n_max(&n_counts);
        
        let mut power = 1;
        while power < min { power <<= 1; }
        
        while power <= max {
            if n_counts == Solution::digit_counts(power) {
                return true;
            }
            
            power <<= 1;
        }
        
        false
    }
    
    /// Returns the smallest number a count of digits can make. Excludes numbers
    /// with leading zeroes.
    fn n_min(counts: &Vec<i32>) -> i32 {
        let mut digits = Vec::new();
        for (n, count) in counts.iter().enumerate() {
            let mut c = 0;
            while c != *count {
                digits.push(n);
                c += 1;
            }
        }
        
        digits.swap(0, counts[0] as usize);
        
        let mut num = 0;
        for d in digits {
            num = num * 10 + d;
        }
        
        num as i32
    }
    
    /// Returns the largest number a count of digits can make.
    fn n_max(counts: &Vec<i32>) -> i32 {
        let mut num = 0;
        for (n, count) in counts.iter().rev().enumerate() {
            let mut c = 0;
            while c != *count {
                num = num * 10 + 9 - n;
                c += 1;
            }
        }
        
        num as i32
    }
    
    /// Returns the digit counts of a given number.
    fn digit_counts(num: i32) -> Vec<i32>{
        let mut num = num;
        let mut counts = vec![0; 10];
        
        while num > 0 {
            counts[(num % 10) as usize] += 1;
            num /= 10;
        }
        
        counts
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn can_reorder_to_power_of_two() {
        assert_eq!(
            Solution::reordered_power_of2(1),
            true
        );
        
        assert_eq!(
            Solution::reordered_power_of2(16),
            true
        );
        
        assert_eq!(
            Solution::reordered_power_of2(46),
            true
        );
        
        assert_eq!(
            Solution::reordered_power_of2(4609),
            true
        );
    }
    
    #[test]
    fn cannot_reorder_to_power_of_two() {
        assert_eq!(
            Solution::reordered_power_of2(10),
            false
        );
        
        assert_eq!(
            Solution::reordered_power_of2(24),
            false
        );
    }
}
