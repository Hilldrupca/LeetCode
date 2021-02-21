pub struct Solution {}

impl Solution {
    
    /// Given a vector of heights, returns the maximum area.
    ///
    /// # Arugments
    /// * 'height' - A vector of i32 heights. The width of an area is the
    /// difference between the height indices.
    ///
    /// # Constraits
    /// * 2 <= n.len() <= 3 * 10^4
    /// * 0 <= height[i] <= 3 * 10^4
    ///
    /// # Examples:
    /// ```
    /// # use crate::container_most_water::Solution;
    /// assert_eq!(Solution::max_area(vec![1,8,6,2,5,4,8,3,7]), 49);
    /// assert_eq!(Solution::max_area(vec![1,1]), 1);
    /// assert_eq!(Solution::max_area(vec![4,3,2,1,4]), 16);
    /// assert_eq!(Solution::max_area(vec![1,2,1]), 2);
    /// ```
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut area = 0;
        let mut front = 0;
        let mut end = height.len() - 1;
        
        while front < end {
            let mut poss = height[front].min(height[end]);
            poss *= (end - front) as i32;
            area = area.max(poss);
            
            if height[front] < height[end] {
                front += 1;
            } else {
                end -= 1;
            }
        }
        
        area
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_max_area() {
        assert_eq!(
            Solution::max_area(vec![1,8,6,2,5,4,8,3,7]),
            49
        );
        
        assert_eq!(
            Solution::max_area(vec![1,1]),
            1
        );
        
        assert_eq!(
            Solution::max_area(vec![4,3,2,1,4]),
            16
        );
        
        assert_eq!(
            Solution::max_area(vec![1,2,1]),
            2
        );
    }
}
