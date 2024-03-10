impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        nums = nums.iter().map(|x| x * x).collect::<Vec<i32>>();
        nums.sort();
        nums
    }
}