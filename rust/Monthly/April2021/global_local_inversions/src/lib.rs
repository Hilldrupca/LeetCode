/// LeetCode Monthly Challenge problem for April 5th, 2021.
pub struct Solution {}

impl Solution {
    
    /// Given some permutation of [0,1, ..., n - 1], returns whether the number
    /// of global inversions is equal to the number of local inversions.
    ///
    /// A global inversion is the number of i < j where 0 <= i < j < N and
    /// A[i] > A[j].
    ///
    /// A local inversion is the number of i where 0 <= i < N and A[i] > A[i+1].
    ///
    /// # Examples
    /// ```
    /// # use crate::global_local_inversions::Solution;
    /// let ex_one = Solution::is_ideal_permutation(
    ///     vec![1,0,2]
    /// );
    /// let ex_two = Solution::is_ideal_permutation(
    ///     vec![1,2,0]
    /// );
    ///
    /// assert_eq!(ex_one, true);
    /// assert_eq!(ex_two, false);
    /// ```
    ///
    /// # Constraints
    /// * a will be a permutation of [0, 1, ..., a.len() - 1]
    /// * a will have length in the range [1, 5000]
    ///
    pub fn is_ideal_permutation(a: Vec<i32>) -> bool {
        let (mut delayed_max, mut prev) = (-1, -1);
        
        for num in a {
            if num < delayed_max {
                return false;
            } else if prev > delayed_max {
                delayed_max = prev;
            }
            
            prev = num;
        }
        
        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn ideal_permuation() {
        assert!(
            Solution::is_ideal_permutation(
                vec![0]
            )
        );
        
        assert!(
            Solution::is_ideal_permutation(
                vec![1,0,2]
            )
        );
    }
    
    #[test]
    fn non_ideal_permuation() {
        assert_eq!(
            Solution::is_ideal_permutation(
                vec![1,2,0]
            ),
            false
        );
    }
}
