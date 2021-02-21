pub struct Solution {}

impl Solution {
    
    /// Converts a decimal integer to a roman numeral.
    ///
    /// # Arguments
    ///
    /// * 'num' - A base 10 integer.
    ///
    /// # Constraints
    /// * 1 <= num <= 3999
    ///
    /// # Examples
    ///
    /// ```
    /// # use crate::integer_to_roman::Solution;
    /// assert_eq!(Solution::int_to_roman(3), "III");
    /// assert_eq!(Solution::int_to_roman(4), "IV");
    /// assert_eq!(Solution::int_to_roman(9), "IX");
    /// assert_eq!(Solution::int_to_roman(58), "LVIII");
    /// assert_eq!(Solution::int_to_roman(1994), "MCMXCIV");
    /// ```
    pub fn int_to_roman(num: i32) -> String {
        let mut res = String::new();
        let mut number: i32 = num;
        
        while number != 0 {
            match number {
                n if n > 999 => { res.push('M'); number -= 1000; },
                n if n > 899 => { res.push_str("CM"); number -= 900; },
                n if n > 499 => { res.push('D'); number -= 500; },
                n if n > 399 => { res.push_str("CD"); number -= 400; },
                n if n > 99 => { res.push('C'); number -= 100; },
                n if n > 89 => { res.push_str("XC"); number -= 90; },
                n if n > 49 => { res.push('L'); number -= 50; },
                n if n > 39 => { res.push_str("XL"); number -= 40; },
                n if n > 9 => { res.push('X'); number -= 10; },
                n if n > 8 => { res.push_str("IX"); number -= 9; },
                n if n > 4 => { res.push('V'); number -= 5; },
                n if n > 3 => { res.push_str("IV"); number -= 4; },
                _ => { res.push('I'); number -= 1; },
            };
        }
        
        res
    }
}

#[cfg(test)]
mod tests {

    use super::*;
    
    #[test]
    fn test_int_to_roman() {
        assert_eq!(
            Solution::int_to_roman(3),
            "III",
        );
        
        assert_eq!(
            Solution::int_to_roman(4),
            "IV",
        );
        
        assert_eq!(
            Solution::int_to_roman(9),
            "IX",
        );
        
        assert_eq!(
            Solution::int_to_roman(58),
            "LVIII",
        );
        
        assert_eq!(
            Solution::int_to_roman(1994),
            "MCMXCIV",
        );
    }
}
