///LeetCode Monthly Challenge problem for March 19th, 2021.
pub struct Solution {}

impl Solution {

    /// Given a vector of rooms numbered from 0 to N, and in each room is a
    /// vector of keys for a specific room, returns whether every room may be
    /// visited.
    ///
    /// Always starts at room 0, which is always unlocked.
    ///
    /// # Arguments
    /// * rooms - A vector of rooms from 0 to N. Each room contains keys to
    /// another room.
    ///
    /// # Examples
    /// ```
    /// # use crate::keys_and_rooms::Solution;
    /// let ex_one = Solution::can_visit_all_rooms(
    ///     vec![
    ///         vec![1],
    ///         vec![2],
    ///         vec![3],
    ///         vec![]
    ///     ]
    /// );
    /// let ex_two = Solution::can_visit_all_rooms(
    ///     vec![
    ///         vec![1,3],
    ///         vec![3,0,1],
    ///         vec![2],
    ///         vec![0]
    ///     ]
    /// );
    ///
    /// assert_eq!(ex_one, true);
    /// assert_eq!(ex_two, false);
    /// ```
    ///
    /// # Constraints
    /// * 1 <= rooms.len() <= 1000
    /// * 0 <= rooms[i].len() <= 1000
    /// * The number of keys in all rooms combined is at most 3000.
    ///
    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        let mut room_count = rooms.len() - 1;
        
        let mut rooms_visited = vec![false; rooms.len()];
        rooms_visited[0] = true;
        
        let mut room_stack: Vec<i32> = Vec::new();
        room_stack.push(0);
        
        while let Some(room) = room_stack.pop() {            
            
            for key in rooms[room as usize].iter() {
                
                if !rooms_visited[*key as usize] {
                    room_count -= 1;
                    rooms_visited[*key as usize] = true;
                    
                    if room_count == 0 {
                        return true;
                    }
                    
                    room_stack.push(*key);
                }
            }
        }
        
        match room_count {
            0 => true,
            _ => false,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn can_visit_all() {
        assert_eq!(
            Solution::can_visit_all_rooms(
                vec![
                    vec![1],
                    vec![2],
                    vec![3],
                    vec![]
                ]
            ),
            true
        );
    }
    
    #[test]
    fn cannot_visit_all() {
        assert_eq!(
            Solution::can_visit_all_rooms(
                vec![
                    vec![1,3],
                    vec![3,0,1],
                    vec![2],
                    vec![0]
                ]
            ),
            false
        );
    }
}
