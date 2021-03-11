/// LeetCode Monthly Challenge problem for March 11th, 2021.
pub struct Solution {}

impl Solution {

    /// Returns the fewest coins that make up the given amount, or -1 if no
    /// combination of coins could make up the amount.
    ///
    /// # Arguments
    /// * coins - A vector of coin values.
    /// * amount - An amount to convert to coins.
    ///
    /// # Examples
    /// ```
    /// # use crate::coin_change::Solution;
    /// let ex_one = Solution::coin_change(vec![1,2,5], 11);
    /// let ex_two = Solution::coin_change(vec![2], 3);
    /// let ex_three = Solution::coin_change(vec![1], 2);
    /// let ex_four = Solution::coin_change(vec![1], 0);
    ///
    /// assert_eq!(ex_one, 3);
    /// assert_eq!(ex_two, -1);
    /// assert_eq!(ex_three, 2);
    /// assert_eq!(ex_four, 0);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= coins.len() <= 12
    /// * 1 <= coins[i] <= 2^31 - 1
    /// * 0 <= amount <= 10^4
    ///
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut res = std::i32::MAX;
        
        let mut coins = coins;
        coins.sort_unstable_by(|a,b| b.cmp(a)); // Sort descending order
        
        let mut stack: Vec<(i32, i32, usize)> = vec![(0, amount, 0)];
        
        while stack.len() > 0 {
            let (count, rem, idx) = stack.pop().unwrap();
            
            if count + rem / coins[idx] + (rem % coins[idx] != 0) as i32 >= res {
                continue;
            } else if rem % coins[idx] == 0 {
                res = res.min(count + rem / coins[idx]);
                continue;
            }
            
            if idx < coins.len() - 1 {
                for c in 0..rem / coins[idx] + 1 {
                    stack.push((count + c, rem - c * coins[idx], idx + 1));
                }
            }
        }
        
        match res {
            std::i32::MAX => -1,
            _ => res,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn zero_amount() {
        assert_eq!(
            Solution::coin_change(vec![1], 0),
            0
        );
    }
    
    #[test]
    fn coin_change_possible() {
        assert_eq!(
            Solution::coin_change(vec![1,2,5], 11),
            3
        );
        
        assert_eq!(
            Solution::coin_change(vec![1], 2),
            2
        );
    }
    
    #[test]
    fn coin_change_not_possible() {
        assert_eq!(
            Solution::coin_change(vec![2], 3),
            -1
        );
    }
}
