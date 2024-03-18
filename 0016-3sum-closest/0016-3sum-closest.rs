use std::cmp;
impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let mut nums = nums;
        let mut distance = 15000;
        let mut ans = 0;
        nums.sort();

        for i in 0..(nums.len() - 2) {
            let n1 = nums[i];
            let (mut j, mut k) = (i + 1, nums.len() - 1);

            while j < k {
                let n2 = nums[j];
                let n3 = nums[k];

                let tmp = n1 + n2 + n3 - target;

                if tmp > 0 {
                    if tmp.abs() < distance {
                        distance = tmp.abs();
                        ans = tmp + target;
                    }
                    k -= 1;
                } else if tmp < 0 {
                    if tmp.abs() < distance {
                        distance = tmp.abs();
                        ans = tmp + target;
                    }
                    j += 1;
                } else {
                    distance = 0;
                    ans = target;
                    return ans;
                }
            }

        }

        ans
    }
}