/// LeetCode Monthly Challenge problem for March 30th, 2021. Not my own work.
/// Required looking solutions with explanations.
pub struct Solution {}

impl Solution {

    /// Returns the maximum number of envelopes that can be put inside one
    /// another. Envelopes cannot be rotated.
    ///
    /// # Examples
    /// ```
    /// # use crate::russian_doll_envelopes::Solution;
    /// let ex_one = Solution::max_envelopes(
    ///     vec![
    ///         vec![5,4],
    ///         vec![6,4],
    ///         vec![6,7],
    ///         vec![2,3]
    ///     ]
    /// );
    /// let ex_two = Solution::max_envelopes(
    ///     vec![
    ///         vec![1,1],
    ///         vec![1,1],
    ///         vec![1,1]
    ///     ]
    /// );
    ///
    /// assert_eq!(ex_one, 3);
    /// assert_eq!(ex_two, 1);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= envelopes.len() <= 5000
    /// * envelopes[i].len() == 2
    /// * 1 <= w, h <= 10^4
    ///
    pub fn max_envelopes(envelopes: Vec<Vec<i32>>) -> i32 {
        let mut envelopes = envelopes;
        envelopes.sort_unstable_by(|a,b| (a[0],-a[1]).cmp(&(b[0],-b[1])));
        
        let mut res = Vec::new();
        
        for envel in envelopes.iter() {
            let left = match res.binary_search(&envel[1]) {
                Ok(a) => a,
                Err(b) => b,
            };
            
            if left == res.len() {
                res.push(envel[1]);
            } else {
                res[left] = envel[1];
            }
        }
        
        res.len() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_max_envelopes() {
        assert_eq!(
            Solution::max_envelopes(
                vec![
                    vec![5,4],
                    vec![6,4],
                    vec![6,7],
                    vec![2,3]
                ]
            ),
            3
        );
        
        assert_eq!(
            Solution::max_envelopes(
                vec![
                    vec![1,1],
                    vec![1,1],
                    vec![1,1]
                ]
            ),
            1
        );
        
        assert_eq!(
            Solution::max_envelopes(
                vec![
                    vec![2,100],
                    vec![3,200],
                    vec![4,300],
                    vec![5,500],
                    vec![5,400],
                    vec![5,250],
                    vec![6,370],
                    vec![6,360],
                    vec![7,380]
                ]
            ),
            5
        );
    }
}
