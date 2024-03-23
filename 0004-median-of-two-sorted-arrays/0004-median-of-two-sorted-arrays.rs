impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (len1, len2) = (nums1.len(), nums2.len());
        let len = len1 + len2;
        let mid = len / 2;

        let (mut i, mut j, mut k) = (0, 0, 0);
        let (mut head, mut tail) = (0, 0);

        while k <= mid {
            tail = head;
            if i == len1 {
                head = nums2[j];
                j += 1;
            } else if j == len2 {
                head = nums1[i];
                i += 1;
            } else if nums1[i] < nums2[j] {
                head = nums1[i];
                i += 1;
            } else {
                head = nums2[j];
                j += 1;
            }
            k += 1;
        }

        if len % 2 == 1 {
            head as f64
        } else {
            ((head + tail) as f64) / 2.0
        }
    }
}