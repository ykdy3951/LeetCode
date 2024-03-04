use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        let mut output : Vec<i32> = Vec::new();

        for i in 0..nums.len() {
            let value = map.get(&(target-nums[i]));
            if value.is_some() {
                output.push(i as i32);
                output.push(*value.unwrap() as i32);
            }
            else {
                map.insert(nums[i], i);
            }
        }

        output
    }
}