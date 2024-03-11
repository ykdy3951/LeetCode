impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        let (mut a, mut b) = (String::new(), String::new());
        for i in s.chars() {
            if i == '#' && a.len() != 0 {
                a.pop();
            }
            else if i != '#' {
                a.push(i);
            }
        }
        for i in t.chars() {
            if i == '#' && b.len() != 0 {
                b.pop();
            }
            else if i != '#' {
                b.push(i);
            }
        }

        a == b
    }
}