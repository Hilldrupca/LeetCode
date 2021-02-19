struct Solution {}

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        // Returns the integer value at the beginning of a string.
        // Similar to C/C++'s atoi function.
        //
        // Integer may be preceeded by the following in presented order:
        // 
        //      multiple spaces (' ')
        //      one sign ('+' or '-'), positive assumed if missing
        //      multiple zeroes ('0')
        //
        // Returns 0 if the above order isn't followed.
        
        let mut res: Option<i32> = None;
        let mut sign: Option<i32> = None;
        
        for c in s.trim().chars() {
            if c.is_numeric() {
            
                // if no sign seen, make positive
                match sign {
                    Some(_) => (),
                    None => sign = Some(1),
                };
                
                let val = (c.to_digit(10).unwrap() as i32) * sign.unwrap();
                
                // initialize res to 0
                match res {
                    Some(_) => (),
                    None => res = Some(0),
                };
                
                // add digit to res
                // if adding digit overflows i32, return min/max
                match res.unwrap().checked_mul(10) {
                    Some(x) => match x.checked_add(val) {
                        Some(y) => res = Some(y),
                        None => {
                            if res.unwrap() > 0 { return std::i32::MAX };
                            if res.unwrap() < 0 { return std::i32::MIN };
                        },
                    },
                    None => {
                        if res.unwrap() > 0 { return std::i32::MAX };
                        if res.unwrap() < 0 { return std::i32::MIN };
                    },
                };
            } else if c == '-' || c == '+' {
                
                // initialize sign if not seen yet
                // break if sign already set
                match sign {
                    None => sign = if c == '-' { Some(-1) } else { Some(1) },
                    Some(_) => break,
                };
            } else {
                break;
            }
        }
        
        match res {
            Some(x) => x,
            None => 0,
        }
    }
}

#[cfg(test)]
mod tests {
    
    use super::*;
    
    #[test]
    fn test_my_atoi() {
        let case_one = String::from("42");
        assert_eq!(
            Solution::my_atoi(case_one),
            42,
        );
        
        let case_two = String::from("   -42");
        assert_eq!(
            Solution::my_atoi(case_two),
            -42,
        );
        
        let case_three = String::from("4193 with words");
        assert_eq!(
            Solution::my_atoi(case_three),
            4193,
        );
        
        let case_four = String::from("words and 987");
        assert_eq!(
            Solution::my_atoi(case_four),
            0,
        );
        
        let case_five = String::from("-91283472332");
        assert_eq!(
            Solution::my_atoi(case_five),
            std::i32::MIN,
        );
        
        let case_six = String::from("- 42");
        assert_eq!(
            Solution::my_atoi(case_six),
            0,
        );
        
        let case_seven = String::from("+1");
        assert_eq!(
            Solution::my_atoi(case_seven),
            1,
        );
        
        let case_eight = String::from("+-12");
        assert_eq!(
            Solution::my_atoi(case_eight),
            0,
        );
        
        let case_nine = String::from("00000-42a1234");
        assert_eq!(
            Solution::my_atoi(case_nine),
            0,
        );
    }
}
