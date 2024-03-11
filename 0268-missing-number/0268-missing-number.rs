impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort();

        for (i, j) in nums.iter().enumerate() {
            if i != *j as usize {
                return i as i32;
            }
        }

        nums.len() as i32
    }
}