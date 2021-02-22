pub struct Solution {}

/// LeetCode Monthly Challenge problem for February 22nd, 2021.
impl Solution {

    /// Given a string, s, and a vector of strings, d, returns the longest
    /// string in d that can be formed from s with zero or more deletions.
    /// If there are two or more possible results, returns the smallest
    /// lexicographical word.
    ///
    /// # Arguments
    /// * s - The base string to form words with.
    /// * d - A vector of strings to form from s.
    ///
    /// # Examples:
    /// ```
    /// # use crate::longest_word_in_dictionary::Solution;
    /// let ex_one = Solution::find_longest_word(
    ///     String::from("abpcplea"),
    ///     vec!["ale".to_string(), "apple".to_string(), "monkey".to_string(), "plea".to_string()],
    /// );
    ///
    /// let ex_two = Solution::find_longest_word(
    ///     String::from("abpcplea"),
    ///     vec!["a".to_string(), "b".to_string(), "c".to_string()],
    /// );
    ///
    /// assert_eq!(ex_one, "apple");
    /// assert_eq!(ex_two, "a");
    /// ```
    ///
    /// # Constraints
    /// * All the strings in the input will only contain lowercase letters.
    /// * The size of d won't exceed 1,000.
    /// * The length of all the strings in the input won't exceed 1,000.
    pub fn find_longest_word(s: String, d: Vec<String>) -> String {
        let mut res = String::new();
        
        for word in d {
            let mut word_iter = word.chars();
            let mut w = word_iter.next();
            
            let mut start_iter = s.chars();
            let mut st = start_iter.next();
            
            while w.is_some() && st.is_some() {
                if w == st {
                    w = word_iter.next();
                }
                
                st = start_iter.next();
            }
            
            if w == None {
                if res.len() < word.len() {
                    res = word;
                } else if res.len() == word.len() {
                    res = res.min(word);
                }
            }
        }
        
        res
    }
}

#[cfg(test)]
mod tests {
    
    use super::*;
    
    #[test]
    fn test_find_longest_word() {
        assert_eq!(
            Solution::find_longest_word(
                String::from("abpcplea"),
                vec!["ale".to_string(), "apple".to_string(), "monkey".to_string(), "plea".to_string()],
            ),
            "apple",
        );
        
        assert_eq!(
            Solution::find_longest_word(
                String::from("abpcplea"),
                vec!["a".to_string(), "b".to_string(), "c".to_string()],
            ),
            "a",
        );
        
        assert_eq!(
            Solution::find_longest_word(
                String::from("a"),
                vec!["b".to_string()],
            ),
            "",
        );
        
        assert_eq!(
            Solution::find_longest_word(
                String::from("aewfafwafjlwajflwajflwafj"),
                vec![
                    "apple".to_string(), "ewaf".to_string(), "awefawfwaf".to_string(),
                    "awef".to_string(), "awefe".to_string(), "ewafeffewafewf".to_string(),
                ],
            ),
            "ewaf",
        );
    }
}
