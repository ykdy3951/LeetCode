impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let l1 = haystack.len();
        let l2 = needle.len();

        if l1 < l2 {
            return -1;
        }

        for i in 0..=(l1-l2) {
            if haystack[i..(i+l2)] == needle {
                return i as i32;
            }
        }

        -1
    }
}