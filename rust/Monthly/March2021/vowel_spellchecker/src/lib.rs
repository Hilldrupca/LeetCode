use std::collections::HashMap;

/// LeetCode Monthly Challenge problem for March 22nd, 2021.
pub struct Solution {}

impl Solution {

    /// Given a vector of correct words, and a vector of querry words, returns
    /// The correct versions of query words if they exist, otherwise an empty
    /// string is returned for that word.
    ///
    /// The following are checked, and the first occurence is returned:
    /// * exact match
    /// * case insensitive
    /// * one or more vowels replaced with other vowels.
    ///
    /// # Examples
    /// ```
    /// # use crate::vowel_spellchecker::Solution;
    /// let ex = Solution::spellchecker(
    ///     vec!["KiTe".to_string(),
    ///          "kite".to_string(),
    ///          "hare".to_string(),
    ///          "Hare".to_string()
    ///     ],
    ///     vec!["kite".to_string(),
    ///          "Kite".to_string(),
    ///          "KiTe".to_string(),
    ///          "Hare".to_string(),
    ///          "HARE".to_string(),
    ///          "Hear".to_string(),
    ///          "hear".to_string(),
    ///          "keti".to_string(),
    ///          "keet".to_string(),
    ///          "keto".to_string()
    ///     ]
    /// );
    ///
    /// assert_eq!(
    ///     ex,
    ///     vec!["kite".to_string(),
    ///          "KiTe".to_string(),
    ///          "KiTe".to_string(),
    ///          "Hare".to_string(),
    ///          "hare".to_string(),
    ///          "".to_string(),
    ///          "".to_string(),
    ///          "KiTe".to_string(),
    ///          "".to_string(),
    ///          "KiTe".to_string()
    ///     ]
    /// );
    /// ```
    ///
    /// # Constraints
    /// * 1 <= wordlist.len() <= 5000
    /// * 1 <= queries.len() <= 5000
    /// * 1 <= wordlist[i].len() <= 7
    /// * 1 <= queries[i].len() <= 7
    /// * All strings in wordlist and queries consist only of english letters.
    ///
    pub fn spellchecker(wordlist: Vec<String>, queries: Vec<String>) -> Vec<String> {
        let poss = Solution::word_possiblities(wordlist);
        let mut res = Vec::new();
        
        for q in queries.iter() {
            if let Some(w) = poss.get(q) {
                res.push(w.clone());
            } else if let Some(x) = poss.get(&q.to_ascii_uppercase()) {
                res.push(x.clone());
            } else if let Some(y) = poss.get(&Solution::vowels_wild(&q)) {
                res.push(y.clone());
            } else {
                res.push(String::new());
            }
        }
        
        res
    }
    
    /// Constructs a hashmap of word possibilities. Maps the case sensitive,
    /// case insensitive, and vowels replaced versions with the first occurence
    /// of the base word.
    fn word_possiblities(wordlist: Vec<String>) -> HashMap<String, String> {
        let mut poss = HashMap::new();
        
        for word in wordlist {
            // case sensitive mapping
            poss.entry(word.clone()).or_insert(word.clone());
            
            // case insensitive mapping
            poss.entry(word.to_ascii_uppercase())
                .or_insert(word.clone());
            
            // vowels are interchangable mapping
            poss.entry(Solution::vowels_wild(&word.to_ascii_lowercase())).or_insert(word);
        }
        
        poss
    }
    
    /// Replaces vowels with an '*', to make them interchangeable.
    fn vowels_wild(word: &String) -> String {
        let mut replaced = String::new();
        let vowels = vec!['a', 'e', 'i', 'o', 'u'];
        
        for c in word.to_ascii_lowercase().chars() {
            if vowels.contains(&c) {
                replaced.push('*');
            } else {
                replaced.push(c);
            }
        }
        
        replaced
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn spellchecker_test() {
     assert_eq!(
         Solution::spellchecker(
            vec!["KiTe".to_string(),
                 "kite".to_string(),
                 "hare".to_string(),
                 "Hare".to_string()
            ],
            vec!["kite".to_string(),
                 "Kite".to_string(),
                 "KiTe".to_string(),
                 "Hare".to_string(),
                 "HARE".to_string(),
                 "Hear".to_string(),
                 "hear".to_string(),
                 "keti".to_string(),
                 "keet".to_string(),
                 "keto".to_string()
            ]
        ),
        vec!["kite".to_string(),
             "KiTe".to_string(),
             "KiTe".to_string(),
             "Hare".to_string(),
             "hare".to_string(),
             "".to_string(),
             "".to_string(),
             "KiTe".to_string(),
             "".to_string(),
             "KiTe".to_string()
        ]
     );
    }
}
