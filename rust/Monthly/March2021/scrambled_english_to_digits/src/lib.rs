/// LeetCode Monthly Challenge problem for March 28th, 2021.
pub struct Solution {}

impl Solution {

    /// Given a non-empty string containing the out-of-order English
    /// representation of digits 0-9, returns the digits in ascending order.
    ///
    /// Note: may not return expected result if string contains extra, or
    /// is missing characters.
    ///
    /// # Examples
    /// ```
    /// # use crate::scrambled_english_to_digits::Solution;
    /// let ex_one = Solution::original_digits("owoztneoer".to_string());
    /// let ex_two = Solution::original_digits("fviefuro".to_string());
    ///
    /// assert_eq!(ex_one, "012".to_string());
    /// assert_eq!(ex_two, "45".to_string());
    /// ```
    ///
    /// # Constraints
    /// * Input contains only lowercase English letters
    /// * Input is guaranteed to be valid and can be transformed to its original
    /// digits. That means invalid inputs such as "abc" or "zerone" are not
    /// permitted.
    /// * Input length is less than 50,000.
    ///
    pub fn original_digits(s: String) -> String {
        let mut chars = vec![0;26];
        
        for c in s.as_bytes() { chars[*c as usize -97] += 1; }
        
        // characters are checked in the following order:
        // z -> w -> u -> o -> f -> x -> s -> g -> t -> n
        let char_order = vec![
            ('0', 25, "zero".to_string()),
            ('2', 22, "two".to_string()),
            ('4', 20, "four".to_string()),
            ('1', 14, "one".to_string()),
            ('5', 5, "five".to_string()),
            ('6', 23, "six".to_string()),
            ('7', 18, "seven".to_string()),
            ('8', 6, "eight".to_string()),
            ('3', 19, "three".to_string()),
            ('9', 4, "nine".to_string())
        ];
        
        let mut digits = Vec::new();
        
        for (digit, char_idx, digit_as_string) in char_order {
            let mut count = chars[char_idx];
            
            for i in digit_as_string.as_bytes() {
                chars[*i as usize - 97] -= count;
            }
            
            while count > 0 {
                digits.push(digit);
                count -= 1;
            }
        }
        
        digits.sort_unstable_by(|a,b| b.cmp(a));
        let mut res = String::new();
        
        while let Some(x) = digits.pop() {
            res.push(x);
        }
        
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_original_digits() {
        assert_eq!(
            Solution::original_digits("owoztneoer".to_string()),
            "012".to_string()
        );
        
        assert_eq!(
            Solution::original_digits("fviefuro".to_string()),
            "45".to_string()
        );
        
        assert_eq!(
            Solution::original_digits(
                "eninthgienevesxisevifruofeerhtowtenoorez".to_string()
            ),
            "0123456789".to_string()
        );
    }
}
