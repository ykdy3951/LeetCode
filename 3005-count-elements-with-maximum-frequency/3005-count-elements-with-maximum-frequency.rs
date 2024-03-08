use std::collections::HashMap;
use std::cmp::Ordering;

impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut map = HashMap::new();
        let mut max_cnt = 0;
        let mut ans = 0;
        for i in nums {
            let tmp_cnt = map.entry(i).or_insert(0);
            *tmp_cnt += 1;

            match (*tmp_cnt).cmp(&max_cnt) {
                Ordering::Greater => {
                    max_cnt = *tmp_cnt;
                    ans = 1;
                },
                Ordering::Equal => {
                    ans += 1;
                }
                _ => ()
            }
        }

        ans * max_cnt
    }
}