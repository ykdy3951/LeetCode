use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let (mut nums1, mut nums2) = (nums1, nums2);
        nums1.sort();
        nums2.sort();
        nums1.dedup();
        nums2.dedup();
        let s1: HashSet<i32> = nums1.into_iter().collect();
        let s2: HashSet<i32> = nums2.into_iter().collect();

        s1.intersection(&s2).cloned().collect()
    }
}