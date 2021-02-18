use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // Returns the indices of the two numbers that sum to the target value.
        // Assumed that each input has exactly one solution.
        //
        // Constraints:
        //      2 <= nums.length() <= 10**3
        //      -10**9 <= nums[i] <= 10**9
        //      -19**9 <= target <= 10**9
        //      only one valid answer exists
        
        let mut res: Vec<i32> = Vec::new();
        let mut compliment: HashMap<i32, i32> = HashMap::new();
        
        for (i, num) in (0..).zip(nums) {
            let comp = target - num;
            
            if compliment.contains_key(&comp) == true {
                res.push(*compliment.get(&comp).unwrap());
                res.push(i);
                break;
            }
            
            compliment.insert(num, i);
            
        }
        
        res
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_two_sum() {
        assert_eq!(
            Solution::two_sum(vec![2,7,11,15], 9),
            vec![0,1]
        );
        
        assert_eq!(
            Solution::two_sum(vec![3,2,4], 6),
            vec![1,2]
        );
        
        assert_eq!(
            Solution::two_sum(vec![3,3], 6),
            vec![0,1]
        );
    }
}
