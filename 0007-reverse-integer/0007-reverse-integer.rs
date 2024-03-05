impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut ans = String::new();
        let mut sb = x.to_string()
            .chars()
            .collect::<Vec<char>>();
        let sign = sb[0] as char;

        if sign == '-' {
            ans.push('-');
            sb.remove(0);
        }

        ans.push_str(
            sb.iter()
                .rev()
                .map(|&c| c as char)
                .collect::<String>()
                .as_str()
            );

        ans.parse::<i32>().unwrap_or(0)
    }
}