impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let ans = x.abs()
            .to_string()
            .chars()
            .rev()
            .collect::<String>()
            .parse::<i32>()
            .unwrap_or(0);

        if x < 0 {
            return ans * -1;
        }

        ans
    }
}