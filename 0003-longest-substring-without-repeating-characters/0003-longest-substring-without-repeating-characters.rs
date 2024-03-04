use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut hash = HashMap::new();
        let mut ans = 0;
        let mut low = -1;

        for (idx, ch) in s.chars().enumerate() {
            if let Some(idx) = hash.insert(ch, idx as i32) {
                low = low.max(idx as i32);
            }
            ans = ans.max(idx as i32  - low);
        }
        ans
    }
}