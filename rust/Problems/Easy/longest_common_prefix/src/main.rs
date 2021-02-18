use std::collections::VecDeque;
use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut words = Vec::new();
        let mut prefix = String::new();
        
        for word in strs {
            let deque: VecDeque<char> = word.chars().collect();
            
            match deque.len() {
                0 => return prefix,
                _ => words.push(deque),
            };
        }
        
        let mut set = HashSet::new();
        
        loop {
            set.clear();
            
            for word in &mut words{
                match word.pop_front() {
                    Some(ch) => set.insert(ch),
                    None => return prefix,
                };
            }
            
            if set.len() == 1 {
                prefix.push(*set.iter()
                               .next()
                               .unwrap());
            } else {
                break;
            }
            
        }
        
        prefix
    }
}

#[cfg(test)]
mod tests {
    
    use super::*;
    
    #[test]
    fn test_longest_common_prefix() {
        assert_eq!(
            Solution::longest_common_prefix(
                vec![String::from("flower"),String::from("flow"), String::from("flight")]
            ),
            "fl",
        );
        
        assert_eq!(
            Solution::longest_common_prefix(
                vec![String::from("dog"), String::from("racecar"), String::from("car")]
            ),
            "",
        );
    }
    
}
