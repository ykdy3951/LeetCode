use std::collections::HashMap;

impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        let mut sum = nums;
        let mut carry = 0;
        let mut ans = 0;

        for i in 0..sum.len() {
            sum[i] += carry;
            if sum[i] == goal {
                ans += 1;
            }
            carry = sum[i];
        }

        for i in 1..sum.len() {
            for j in i..sum.len() {
                if sum[j] > goal + sum[i-1] {
                    break;
                }
                else if sum[j] == goal + sum[i-1] {
                    ans+=1;
                }
            }
        }
        ans
    }
}