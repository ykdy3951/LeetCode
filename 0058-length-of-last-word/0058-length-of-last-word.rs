impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        s.split_whitespace().rev().collect::<Vec<&str>>()[0].len() as i32
    }
}