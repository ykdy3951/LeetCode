use std::cmp::Ordering;

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let (mut left, mut right) = (0, nums.len()-1);

        while left < right {
            let mid = (left + right) >> 1;

            match nums[mid].cmp(&target) {
                Ordering::Less => left = mid + 1,
                Ordering::Equal => break,
                Ordering::Greater => right = mid,
            }
        }

        let mid = (left + right) >> 1;
        if nums[mid] >= target {
            return mid as i32;
        }
        (mid + 1) as i32
    }
}