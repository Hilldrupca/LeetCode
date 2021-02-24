pub struct Solution {}

/// LeetCode Monthly Challenge problem for February 24th, 2021.
impl Solution {

    /// Given a balanced parentheses String, computes the score of the string
    /// based on the following rules:
    /// * () has a score of 1
    /// * AB has a score of A + B, where A and B are balanced parentheses strings
    /// * (A) has a score of 2 * A, where A is a balanced parentheses string
    ///
    /// # Arguments
    /// * s - A balanced parentheses string.
    ///
    /// # Examples
    /// ```
    /// # use crate::score_of_parentheses::Solution;
    /// let ex_one = Solution::score_of_parentheses(String::from("()"));
    /// let ex_two = Solution::score_of_parentheses(String::from("(())"));
    /// let ex_three = Solution::score_of_parentheses(String::from("()()"));
    /// let ex_four = Solution::score_of_parentheses(String::from("(()(()))"));
    ///
    /// assert_eq!(ex_one, 1);
    /// assert_eq!(ex_two, 2);
    /// assert_eq!(ex_three, 2);
    /// assert_eq!(ex_four, 6);
    /// ```
    ///
    /// # Constraints
    /// * s is a balanced parentheses string, containing only '(' and ')'.
    /// * 2 <= s.len() <= 50
    ///
    pub fn score_of_parentheses(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut res: i32 = 0;
        
        let mut i = 0;
        
        while i < chars.len() {
            res += Solution::score_helper(&chars, &mut i);
            i += 1;
        }
        
        res
    }
    
    /// A helper method for score_of_parentheses() that will recursively find
    /// the score for different levels in the parentheses stack.
    fn score_helper(parens: &Vec<char>, i: &mut usize) -> i32 {
        let mut group: i32 = 0;
        
        *i += 1;
        
        if parens[*i] == ')' {
            group = 1;
        } else {
            while parens[*i] != ')' {
                group += 2 * Solution::score_helper(parens, i);
                *i += 1;
            }
        }
        
        group
    }
}

#[cfg(test)]
mod tests {

    use super::*;
    
    #[test]
    fn test_score_of_parentheses() {
        assert_eq!(
            Solution::score_of_parentheses(String::from("()")),
            1,
        );
        
        assert_eq!(
            Solution::score_of_parentheses(String::from("(())")),
            2,
        );
        
        assert_eq!(
            Solution::score_of_parentheses(String::from("()()")),
            2,
        );
        
        assert_eq!(
            Solution::score_of_parentheses(String::from("(()(()))")),
            6,
        );
    }
}
