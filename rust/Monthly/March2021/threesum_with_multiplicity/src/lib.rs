/// LeetCode Monthly Challenge problem for March 23rd, 2021.
pub struct Solution {}

impl Solution {

    /// Given an integer array arr, and an integer target, returns the number
    /// of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] ==
    /// target.
    ///
    /// As the answer can be very large, return it modulo 109 + 7.
    ///
    /// # Examples
    /// ```
    /// # use crate::threesum_with_multiplicity::Solution;
    /// let ex_one = Solution::three_sum_multi(vec![1,1,2,2,3,3,4,4,5,5], 8);
    /// let ex_two = Solution::three_sum_multi(vec![1,1,2,2,2,2], 5);
    ///
    /// assert_eq!(ex_one, 20);
    /// assert_eq!(ex_two, 12);
    /// ```
    ///
    /// # Arguments
    /// * 3 <= arr.len() <= 3000
    /// * 0 <= arr[i] <= 100
    /// * 0 <= target <= 300
    ///
    pub fn three_sum_multi(arr: Vec<i32>, target: i32) -> i32 {
        let mut counts: Vec<usize> = vec![0;101];
        let mut res = 0;
        
        for n in arr { counts[n as usize] += 1; }
        
        for i in 0..counts.len() {
            let (mut j, mut k) = (i, counts.len() - 1);
            
            while j <= k && k < counts.len() && j < counts.len() {
                let sum = (i + j + k) as i32;
                
                if sum < target {
                    j += 1;
                } else if sum > target {
                    k -= 1;
                } else {
                    
                    if i == j && j == k && counts[i] > 2 {
                        res += counts[i] * (counts[i] - 1) * (counts[i] - 2) / 6;
                    } else if i == j && j != k && counts[j] > 1 {
                        res += counts[j] * (counts[j] - 1) * counts[k] / 2;
                    } else if i != k && j == k && counts[j] > 1 {
                        res += counts[i] * counts[j] * (counts[j] - 1) / 2;
                    } else if i != j && j != k{
                        res += counts[i] * counts[j] * counts[k];
                    }
                    
                    j += 1;
                    k -= 1;
                }
            }
            
        }
        
        (res % (10_usize.pow(9) + 7)) as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_three_sum_multi() {
        assert_eq!(
            Solution::three_sum_multi(vec![1,1,2,2,3,3,4,4,5,5], 8),
            20
        );
        
        assert_eq!(
            Solution::three_sum_multi(vec![1,1,2,2,2,2], 5),
            12
        );
        
        assert_eq!(
            Solution::three_sum_multi(vec![2,2,3,2], 7),
            3
        );
        
        assert_eq!(
            Solution::three_sum_multi(vec![2,1,3], 6),
            1
        );
        
        assert_eq!(
            Solution::three_sum_multi(vec![3,3,0,0,3,2,2,3], 6),
            12
        );
    }
}
