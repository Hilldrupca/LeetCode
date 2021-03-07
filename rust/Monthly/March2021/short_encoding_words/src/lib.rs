/// LeetCode Monthly Challenge problem for March 6th, 2021.

pub struct Solution {}

impl Solution {

    /// Returns the shortest length of any possible valid enoding of words.
    /// 
    /// Shortest encoding is done by finding parent words, and child words.
    /// A parent word is any word that ends with a child word. "time" is a
    /// parent word of "me". Once all parent words are found a '#' is appended
    /// to each, and all lengths are summed and returned.
    ///
    /// # Arguments
    /// * words - A vector of strings.
    ///
    /// # Examples
    /// ```
    /// # use crate::short_encoding_words::Solution;
    /// let ex_one = Solution::minimum_length_encoding(
    ///     vec!["time".to_string(), "me".to_string(), "bell".to_string()]
    /// );
    /// let ex_two = Solution::minimum_length_encoding(
    ///     vec!["t".to_string()]
    /// );
    ///
    /// assert_eq!(ex_one, 10);     // "time#bell#" or "bell#time#"
    /// assert_eq!(ex_two, 2);      // "t#"
    /// ```
    ///
    /// # Constraints
    /// * 1 <= words.len() <= 2000
    /// * 1 <= words[i].len() <= 7
    /// * words[i] consists of only lowercase letters.
    pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
        let mut words = words;
        
        // Reverse each string
        words = words.into_iter()
                     .map(|w| w.chars().rev().collect())
                     .collect();
    
        // Sort strings by descending order
        words.sort_unstable_by(|a,b| b.cmp(a));
        
        let mut res = 0;
        
        while !words.is_empty() {
            let mut w = words.pop().unwrap();
            
            while let Some(last) = words.last() {
                match last.starts_with(&w){
                    true => w = words.pop().unwrap(),
                    false => break,
                };
            }
            
            res += w.len() + 1; // 1 accounts for the length of '#'
        }

        res as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn multiple_words() {
        assert_eq!(
            Solution::minimum_length_encoding(
                vec!["time".to_string(), "me".to_string(), "bell".to_string()],
            ),
            10,
        );
    }
    
    #[test]
    fn single_word() {
        assert_eq!(
            Solution::minimum_length_encoding(
                vec!["t".to_string()],
            ),
            2,
        );
    }
    
    #[test]
    fn zero_words() {
        assert_eq!(
            Solution::minimum_length_encoding(vec![]),
            0,
        );
    }
}
