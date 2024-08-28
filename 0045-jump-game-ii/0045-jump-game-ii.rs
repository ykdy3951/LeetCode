use std::cmp::min;

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        
        const MAX : i32 = 10005;

        let len : usize = nums.len();
        let mut dp = vec![MAX; len];
        
        dp[0] = 0;

        for i in 0..len {
            let val = min(len - 1, nums[i] as usize + i);

            for j in i+1..=val {
                dp[j] = min(dp[i] + 1, dp[j]);
            }
        }

        dp[len-1]
    }
}