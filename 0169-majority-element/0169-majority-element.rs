impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let (mut val, mut cnt) = (nums[0], 0);
        for i in nums {
            if val == i {
                cnt += 1;
            } else if cnt > 0 {
                cnt -= 1;
            } else {
                val = i;
                cnt = 1;
            }

        }

        val
    }
}