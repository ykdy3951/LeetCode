use std::collections::VecDeque;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = VecDeque::new();
        for c in s.chars() {
            match c {
                '(' | '[' | '{' => stack.push_back(c),
                ')' => {
                    if stack.pop_back() != Some('(') {
                        return false;
                    }
                }
                ']' => {
                    if stack.pop_back() != Some('[') {
                        return false;
                    }
                }
                '}' => {
                    if stack.pop_back() != Some('{') {
                        return false;
                    }
                }
                _ => {}
            }
        }
        if stack.is_empty() {
            true
        } else {
            false
        }
    }
}