/// LeetCode Monthly Challenge problem for April 7th, 2021.
pub struct Solution {}

impl Solution {

    /// Returns whether the halves of a string are alike. String halves are
    /// alike if they have the same vowel counts ('a', 'e', 'i', 'o', 'u').
    ///
    /// # Examples
    /// ```
    /// # use crate::string_halves_alike::Solution;
    /// let ex_one = Solution::halves_are_alike("book".to_string());
    /// let ex_two = Solution::halves_are_alike("textbook".to_string());
    ///
    /// assert_eq!(ex_one, true);
    /// assert_eq!(ex_two, false);
    /// ```
    ///
    /// # Constraints
    /// * 2 <= s.len() <= 1000
    /// * s.len() is even           // should work for odd lengths too.
    /// * s consists of uppercase and lowercase letters.
    ///
    pub fn halves_are_alike(s: String) -> bool {
        let mut char_bytes = Vec::with_capacity(s.len());
        for byte in s.to_lowercase().as_bytes() {
            char_bytes.push(*byte - 97);
        }
        
        let mut front = [0;26];
        let mut back = [0;26];
        let (mut i, mut j) = (0, s.len() - 1);
        
        while i < j {
            front[char_bytes[i] as usize] += 1;
            back[char_bytes[j] as usize] += 1;
            i += 1;
            j -= 1;
        }
        
        
        let front_count = front[0] + front[4] + front[8] + front[14] + front[20];
        let back_count = back[0] + back[4] + back[8] + back[14] + back[20];
        
        front_count == back_count
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn string_halves_are_alike() {
        assert_eq!(
            Solution::halves_are_alike("book".to_string()),
            true
        );
        
        assert_eq!(
            Solution::halves_are_alike("AbCdEfGh".to_string()),
            true
        );
    }
    
    #[test]
    fn string_halves_are_not_alike() {
        assert_eq!(
            Solution::halves_are_alike("textbook".to_string()),
            false
        );
        
        assert_eq!(
            Solution::halves_are_alike("MerryPoppins".to_string()),
            false
        );
    }
}
