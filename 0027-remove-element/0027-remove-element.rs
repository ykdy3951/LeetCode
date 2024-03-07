impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        *nums = nums.into_iter().filter(|x| **x != val).map(|x| *x).collect();
        nums.len() as i32
    }
}