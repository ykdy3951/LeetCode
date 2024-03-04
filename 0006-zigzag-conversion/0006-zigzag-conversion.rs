impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 {
            return s;
        }

        let mut ans = String::new();
        let mid = num_rows - 1;
        let k = 2 * mid;

        for i in 0..=mid {
            for (idx, ch) in s.chars().enumerate() {
                let moded_idx = (idx as i32) % k;

                if (moded_idx == i) || (moded_idx == k - i) {
                    ans.push(ch);
                }
            }
        }
        ans
    }
}