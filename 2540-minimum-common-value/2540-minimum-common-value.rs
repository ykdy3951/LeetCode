use std::cmp::Ordering;

impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (mut nums1, mut nums2) = (nums1, nums2);
        nums1.sort();
        nums2.sort();
        let (mut i, mut j) = (0, 0);

        while i < nums1.len() && j < nums2.len() {
            match nums1[i].cmp(&nums2[j]) {
                Ordering::Less => i += 1,
                Ordering::Greater => j += 1,
                Ordering::Equal => return nums1[i],
            }
        }

        -1
    }
}