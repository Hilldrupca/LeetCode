/// LeetCode Monthly Challenge problem for March 12th, 2021.
/// Not an original answer. First successful submissions used a hashset which
/// was quite slow
pub struct Solution {}

impl Solution {

    /// Returns whether the given strings contains all binary codes of length k.
    ///
    /// # Arguments
    /// * s - A string containing ones, and zeroes only.
    /// * k - binary code length.
    ///
    /// # Examples
    /// ```
    /// # use crate::string_contains_all_k_length_binary::Solution;
    /// let ex_one = Solution::has_all_codes("00110110".to_string(), 2);
    /// let ex_two = Solution::has_all_codes("00110".to_string(), 2);
    /// let ex_three = Solution::has_all_codes("0110".to_string(), 1);
    /// let ex_four = Solution::has_all_codes("0110".to_string(), 2);
    /// let ex_five = Solution::has_all_codes("0000000001011100".to_string(), 4);
    ///
    /// assert_eq!(ex_one, true);
    /// assert_eq!(ex_two, true);
    /// assert_eq!(ex_three, true);
    /// assert_eq!(ex_four, false);
    /// assert_eq!(ex_five, false);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= s.len() <= 5 * 10^5
    /// * s consists of 0's and 1's only.
    /// * 1 <= k <= 20
    ///
    pub fn has_all_codes(s: String, k: i32) -> bool {
        let mut lim = 1 << k;
        let ones = lim - 1;
        
        let mut seen = vec![false; lim as usize];
        let mut hash = 0;
        
        for i in 0..s.len() {
            hash = (hash << 1 & ones) | (s.as_bytes()[i] - b'0') as i32;
            
            if i as i32 >= k - 1 && !seen[hash as usize] {
                seen[hash as usize] = true;
                lim -= 1;
                
                if lim == 0 { return true; }
            }
        }
        
        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn contains_all_codes() {
        assert_eq!(
            Solution::has_all_codes("00110110".to_string(), 2),
            true
        );
        
        assert_eq!(
            Solution::has_all_codes("00110".to_string(), 2),
            true
        );
        
        assert_eq!(
            Solution::has_all_codes("0110".to_string(), 1),
            true
        );
    }
    
    #[test]
    fn does_not_contain_all_codes() {
        assert_eq!(
            Solution::has_all_codes("0110".to_string(), 2),
            false
        );
        
        assert_eq!(
            Solution::has_all_codes("0000000001011100".to_string(), 4),
            false
        );
    }
}
