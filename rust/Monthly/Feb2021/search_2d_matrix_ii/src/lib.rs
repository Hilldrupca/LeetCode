pub struct Solution {}

/// LeetCode Monthly Challenge problem for February 23rd, 2021.
impl Solution {

    /// Searches an M x N matrix for a target value. Returns true if the value
    /// is found, and false if not.
    ///
    /// # Arguments
    /// * matrix - An M x N vector of i32 vectors.
    /// * target - The target i32 value to search for.
    ///
    /// # Examples:
    /// ```
    /// # use crate::search_2d_matrix_ii::Solution;
    /// let matrix = vec![vec![1,4,7,11,15],
    ///                   vec![2,5,8,12,19],
    ///                   vec![3,6,9,16,22],
    ///                   vec![10,13,14,17,24],
    ///                   vec![18,21,23,26,30]];
    /// 
    /// let matrix_copy = matrix.to_owned();
    ///
    /// assert_eq!(Solution::search_matrix(matrix, 5), true);
    /// assert_eq!(Solution::search_matrix(matrix_copy, 20), false);
    /// ```
    ///
    /// # Constraints
    /// * m == matrix.len()
    /// * n == matrix[i].len()
    /// * 1 <= n, m <= 300
    /// * -10^9 <= matrix[i][j] <= 10^9
    /// * All the integers in each row are sorted in ascending order.
    /// * All the integers in each column are sorted in ascending order.
    /// * -10^9 <= targert <= 10^9
    ///
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        for row in matrix {
            if row[0] <= target && target <= row[row.len() - 1] {
                match row.binary_search(&target) {
                    Ok(_) => return true,
                    Err(_) => (),
                };
            } else if row[0] > target {
                break;
            }
        }
        
        false
    }
}


#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_search_matrix() {
        let matrix = vec![vec![1,4,7,11,15],
                          vec![2,5,8,12,19],
                          vec![3,6,9,16,22],
                          vec![10,13,14,17,24],
                          vec![18,21,23,26,30]];
                          
        let matrix_2 = matrix.to_owned();
                          
        assert_eq!(Solution::search_matrix(matrix, 5), true);
        
        assert_eq!(Solution::search_matrix(matrix_2, 20), false);
    }
}
