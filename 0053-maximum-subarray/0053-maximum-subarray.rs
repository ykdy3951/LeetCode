use std::cmp::max;

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {

        let len : usize = nums.len();
        let mut dp = vec![vec![-1;len];2];

        Self::recv_fn(0, false, len, &nums, &mut dp)
    }

    fn recv_fn(idx : usize, is_include : bool, len : usize, nums : & Vec<i32>, dp : &mut Vec<Vec<i32>>) -> i32 {
        if idx >= len {
            return if is_include {0} else {-1e5 as i32};
        }

        if dp[is_include as usize][idx] != -1 {
            return dp[is_include as usize][idx];
        }

        if is_include {
            dp[is_include as usize][idx] = max(0, nums[idx] + Self::recv_fn(idx + 1, true, len, nums, dp));
            return dp[is_include as usize][idx];
        }

        dp[is_include as usize][idx] = max(Self::recv_fn(idx + 1, false, len, nums, dp), nums[idx] + Self::recv_fn(idx + 1, true, len, nums, dp));
        return dp[is_include as usize][idx];
    }
}