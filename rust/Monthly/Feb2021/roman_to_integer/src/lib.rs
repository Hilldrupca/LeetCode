pub struct Solution {}

/// LeetCode Monthly Challenge problem for February 20th, 2021
impl Solution {
    
    /// Converts the roman numeral to an integer.
    ///
    /// # Arguments
    ///
    /// * 's' - A string consisting of the roman numerals I, V, X, L, C, D, and/or M
    ///
    /// # Examples
    ///
    /// ```
    /// # use crate::roman_to_integer::Solution;
    /// let three = String::from("III");
    /// let four = String::from("IV");
    /// let nine = String::from("IX");
    /// let fifty_eight = String::from("LVIII");
    /// let nineteen_ninety_four = String::from("MCMXCIV");
    /// 
    /// assert_eq!(Solution::roman_to_int(three), 3);
    /// assert_eq!(Solution::roman_to_int(four), 4);
    /// assert_eq!(Solution::roman_to_int(nine), 9);
    /// assert_eq!(Solution::roman_to_int(fifty_eight), 58);
    /// assert_eq!(Solution::roman_to_int(nineteen_ninety_four), 1994);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= s.len() <= 15
    /// * It is guaranteed that s is a valid roman numeral in the range [1, 3999]
    ///
    pub fn roman_to_int(s: String) -> i32 {
        let mut res: Vec<i32> = Vec::new();
        
        for c in s.chars() {
            let mut val: i32 = match c {
                'I' => 1,
                'V' => 5,
                'X' => 10,
                'L' => 50,
                'C' => 100,
                'D' => 500,
                'M' => 1000,
                _ => continue,
            };
            
            match res.last() {
                Some(x) => {
                    if x < &val {
                        val -= res.pop().unwrap();
                        res.push(val);
                    } else {
                        res.push(val);
                    }
                },
                None => res.push(val),
            };
        }
        
        res.iter().sum()
    }
}

#[cfg(test)]
mod test {
    
    use super::*;
    
    #[test]
    fn test_roman_to_int() {
        
        assert_eq!(
            Solution::roman_to_int(String::from("III")),
            3,
        );
        
        assert_eq!(
            Solution::roman_to_int(String::from("IV")),
            4,
        );
        
        assert_eq!(
            Solution::roman_to_int(String::from("IX")),
            9,
        );
        
        assert_eq!(
            Solution::roman_to_int(String::from("LVIII")),
            58,
        );
        
        assert_eq!(
            Solution::roman_to_int(String::from("MCMXCIV")),
            1994,
        );
    }
    
}
