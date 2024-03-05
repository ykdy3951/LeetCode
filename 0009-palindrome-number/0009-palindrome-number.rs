impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let s = x.to_string();
        let sb = s.as_bytes();

        sb.iter().eq(sb.iter().rev())
    }
}