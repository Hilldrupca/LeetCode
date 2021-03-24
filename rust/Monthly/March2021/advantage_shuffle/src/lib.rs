/// LeetCode Monthly Challenge problem for March 24th, 2021.
pub struct Solution {}

impl Solution {

    /// Given two arrays A and B of equal size, the advantage of A with respect
    /// to B is the number of indices i for which A[i] > B[i].
    ///
    /// Returns a permutation of A that maximizes its advantage with respect
    /// to B.
    /// 
    /// Note: This does not return a random permutation. The results will be the
    /// same for each unique pairs of given vectors.
    ///
    /// # Examples
    /// ```
    /// # use crate::advantage_shuffle::Solution;
    /// let ex_one = Solution::advantage_count(
    ///     vec![2,7,11,15],
    ///     vec![1,10,4,11]
    /// );
    /// let ex_two = Solution::advantage_count(
    ///     vec![12,24,8,32],
    ///     vec![13,25,32,11]
    /// );
    ///
    /// assert_eq!(ex_one, vec![2,11,7,15]);
    /// assert_eq!(ex_two, vec![24,32,8,12]);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= a.len() = b.len() <= 10000
    /// * 0 <= a[i] <= 10^9
    /// * 0 <= b[i] <= 10^9
    ///
    pub fn advantage_count(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let mut res = vec![-1;a.len()];
        let mut b_idx_pairs = Vec::new();
        
        for (idx, num) in b.iter().enumerate() {
            b_idx_pairs.push((num, idx));
        }
        
        let mut a_sorted = a;
        a_sorted.sort_unstable();
        b_idx_pairs.sort_unstable();
        
        let mut idx = b_idx_pairs.len();
        while idx > 0 {
            idx -= 1;
            
            if a_sorted.last().unwrap() > b_idx_pairs[idx].0 {
                res[b_idx_pairs[idx].1] = a_sorted.pop().unwrap();
            }
        }
        
        for i in 0..res.len() {
            if res[i] == -1 {
                res[i] = a_sorted.pop().unwrap();
            }
        }
        
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_advantage_shuffle() {
        assert_eq!(
            Solution::advantage_count(
                vec![2,7,11,15],
                vec![1,10,4,11]
            ),
            vec![2,11,7,15]
        );
        
        assert_eq!(
            Solution::advantage_count(
                vec![12,24,8,32],
                vec![13,25,32,11]
            ),
            vec![24,32,8,12]
        );
    }
}
