/// LeetCode Monthly Challenge problem for March 26th, 2021.
pub struct Solution {}

impl Solution {

    /// Given two vectors of strings A, and B, returns all words from A where
    /// every word in B is a subset of A.
    ///
    /// # Examples
    /// ```
    /// # use crate::word_subsets::Solution;
    /// let ex_one = Solution::word_subsets(
    ///     vec!["amazon".to_string(),
    ///          "apple".to_string(),
    ///          "facebook".to_string(),
    ///          "google".to_string(),
    ///          "leetcode".to_string()
    ///     ],
    ///     vec!["e".to_string(), "o".to_string()]
    /// );
    /// let ex_two = Solution::word_subsets(
    ///     vec!["amazon".to_string(),
    ///          "apple".to_string(),
    ///          "facebook".to_string(),
    ///          "google".to_string(),
    ///          "leetcode".to_string()
    ///     ],
    ///     vec!["ec".to_string(), "oc".to_string(), "ceo".to_string()]
    /// );
    ///
    /// assert_eq!(
    ///     ex_one,
    ///     vec!["facebook".to_string(), "google".to_string(), "leetcode".to_string()]
    /// );
    /// assert_eq!(
    ///     ex_two,
    ///     vec!["facebook".to_string(), "leetcode".to_string()]
    /// );
    /// ```
    ///
    /// # Constraints
    /// * 1 <= A.len(), B.len() <= 10000
    /// * 1 <= A[i].len(), B[i].len() <= 10
    /// * A[i] and B[i] consist only of lowercase letters.
    /// * All words in A[i] are unique
    ///
    pub fn word_subsets(a: Vec<String>, b: Vec<String>) -> Vec<String> {
        let char_counts = Solution::max_char_counts(b);
        let mut res = Vec::new();
        
        for word in a {
            let counts = Solution::char_freq(&word);
            let mut universal = true;
            
            for i in 0..26 {
                if char_counts[i] > counts[i] {
                    universal = false;
                    break;
                }
            }
            
            if universal { res.push(word); }
        }
        
        res
    }
    
    /// Returns the character frequencies of a string.
    fn char_freq(word: &String) -> Vec<u16> {
        let mut counts = vec![0;26];
        for c in word.as_bytes() {
            counts[*c as usize - 97] += 1;
        }
        
        counts
    }
    
    /// Returns the maximum character frequencies of a vector of strings.
    fn max_char_counts(words: Vec<String>) -> Vec<u16> {
        let mut counts = vec![0;26];
        
        for word in words.iter() {
            let mut cur = vec![0;26];
            
            for c in word.as_bytes() {
                let c_num = *c as usize - 97;
                cur[c_num] += 1;
                
                if cur[c_num] > counts[c_num] {
                    counts[c_num] = cur[c_num];
                }
            }
        }
        
        counts
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_word_subsets() {
        assert_eq!(
            Solution::word_subsets(
                vec![
                    "amazon".to_string(),
                    "apple".to_string(),
                    "facebook".to_string(),
                    "google".to_string(),
                    "leetcode".to_string()
                ],
                vec![
                    "e".to_string(),
                    "o".to_string()
                ]
            ),
            vec![
                "facebook".to_string(),
                "google".to_string(),
                "leetcode".to_string()
            ]
        );
        
        assert_eq!(
            Solution::word_subsets(
                vec![
                    "amazon".to_string(),
                    "apple".to_string(),
                    "facebook".to_string(),
                    "google".to_string(),
                    "leetcode".to_string()
                ],
                vec![
                    "l".to_string(),
                    "e".to_string()
                ]
            ),
            vec![
                "apple".to_string(),
                "google".to_string(),
                "leetcode".to_string()
            ]
        );
        
        assert_eq!(
            Solution::word_subsets(
                vec![
                    "amazon".to_string(),
                    "apple".to_string(),
                    "facebook".to_string(),
                    "google".to_string(),
                    "leetcode".to_string()
                ],
                vec![
                    "e".to_string(),
                    "oo".to_string()
                ]
            ),
            vec![
                "facebook".to_string(),
                "google".to_string()
            ]
        );
        
        assert_eq!(
            Solution::word_subsets(
                vec![
                    "amazon".to_string(),
                    "apple".to_string(),
                    "facebook".to_string(),
                    "google".to_string(),
                    "leetcode".to_string()
                ],
                vec![
                    "lo".to_string(),
                    "eo".to_string()
                ]
            ),
            vec![
                "google".to_string(),
                "leetcode".to_string()
            ]
        );
        
        assert_eq!(
            Solution::word_subsets(
                vec![
                    "amazon".to_string(),
                    "apple".to_string(),
                    "facebook".to_string(),
                    "google".to_string(),
                    "leetcode".to_string()
                ],
                vec![
                    "ec".to_string(),
                    "oc".to_string(),
                    "ceo".to_string()
                ]
            ),
            vec![
                "facebook".to_string(),
                "leetcode".to_string()
            ]
        );
    }
}
