struct Solution {}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        // Returns whether the given number is a palindrome. if a negative
        // number is given, the sign position is not preserved. So "-1"
        // reversed becomes "1-".
    
        let forward: String = x.to_string();
        let backward: String = forward.chars()
                                      .rev()
                                      .collect();
        
        forward == backward
    }
}

#[cfg(test)]
mod tests {
    
    use super::*;
    
    #[test]
    fn test_is_palindrome() {
        assert_eq!(
            Solution::is_palindrome(121_i32),
            true,
        );
        
        assert_eq!(
            Solution::is_palindrome(-121_i32),
            false,
        );
        
        assert_eq!(
            Solution::is_palindrome(10),
            false,
        );
        
        assert_eq!(
            Solution::is_palindrome(-101),
            false,
        );
    }
}
