impl Solution {
    pub fn merge(mut nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut ans = Vec::new();
        let (mut m, mut n) = (m, n);
        while m > 0 || n > 0 {
            if m == 0 {
                ans.push(nums2[0]);
                nums2.remove(0);
                n -= 1;
            } else if n == 0 {
                ans.push(nums1[0]);
                nums1.remove(0);
                m -= 1;
            } else if nums1[0] > nums2[0] {
                ans.push(nums2[0]);
                nums2.remove(0);
                n -= 1;
            } else {
                ans.push(nums1[0]);
                nums1.remove(0);
                m -= 1;
            }
        }
        *nums1 = ans;
    }
}
