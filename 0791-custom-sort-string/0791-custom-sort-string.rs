use std::collections::HashMap;
impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut map = HashMap::new();
        for i in s.chars() {
            let value = map.entry(i).or_insert(0);
            *value += 1;
        }
        let mut ans = String::new();
        for i in order.chars() {
            if let Some(val) = map.get(&i) {
                for _ in 0..*val {
                    ans.push(i);
                }
                map.insert(i, 0);
            }
        }

        for (key, val) in map.iter() {
            if *val > 0 {
                for _ in 0..*val {
                    ans.push(*key);
                }
            }
        }

        ans
    }
}