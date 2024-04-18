impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut len = 1;
        for i in 1..nums.len() {
            if len == 1 || nums[i] != nums[len-2] {
                nums[len] = nums[i];
                len += 1;
            }
        }
        len as i32
    }
}