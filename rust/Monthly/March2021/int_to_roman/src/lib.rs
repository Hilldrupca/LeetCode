///LeetCode Monthly Challenge problem for March 10th, 2021.
pub struct Solution {}

impl Solution {

    /// Returns the roman numeral version of a given integer.
    ///
    /// # Arguments
    /// * num - An integer value to convert to a roman numeral.
    ///
    /// # Examples
    /// ```
    /// # use crate::int_to_roman::Solution;
    /// let ex_one = Solution::int_to_roman(3);
    /// let ex_two = Solution::int_to_roman(4);
    /// let ex_three = Solution::int_to_roman(9);
    /// let ex_four = Solution::int_to_roman(58);
    /// let ex_five = Solution:: int_to_roman(1994);
    ///
    /// assert_eq!(ex_one, "III".to_string());
    /// assert_eq!(ex_two, "IV".to_string());
    /// assert_eq!(ex_three, "IX".to_string());
    /// assert_eq!(ex_four, "LVIII".to_string());
    /// assert_eq!(ex_five, "MCMXCIV".to_string());
    /// ```
    ///
    /// # Constraints
    /// * 1 <= num <= 3999
    ///
    pub fn int_to_roman(num: i32) -> String {
        let dec_numeral_map = vec![
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ];
        
        let mut num = num;
        let mut res = String::new();
        
        for (dec, numeral) in dec_numeral_map {
            while num / dec > 0 {
                res.push_str(numeral);
                num -= dec;
            }
        }
        
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn three_to_roman() {
        assert_eq!(
            Solution::int_to_roman(3),
            "III".to_string()
        );
    }
    
    #[test]
    fn four_to_roman() {
        assert_eq!(
            Solution::int_to_roman(4),
            "IV".to_string()
        );
    }
    
    #[test]
    fn nine_to_roman() {
        assert_eq!(
            Solution::int_to_roman(9),
            "IX".to_string()
        );
    }
    
    #[test]
    fn fifty_eight_to_roman() {
        assert_eq!(
            Solution::int_to_roman(58),
            "LVIII".to_string()
        );
    }
    
    #[test]
    fn nineteen_ninety_four_to_roman() {
        assert_eq!(
            Solution::int_to_roman(1994),
            "MCMXCIV".to_string()
        );
    }
}
