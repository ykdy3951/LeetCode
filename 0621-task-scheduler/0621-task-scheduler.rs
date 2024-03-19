use std::collections::HashMap;

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        if tasks.len() == 1 {
            return 1;
        }

        let mut map = HashMap::new();
        for i in tasks.clone() {
            let val = map.entry(i).or_insert(0);
            *val += 1;
        }

        let mut values: Vec<i32> = map.into_values().collect();
        values.sort_by(|a, b| b.cmp(a));
        let max = values[0];
        let cnt = values.iter().filter(|&x| *x == max).count() as i32;

        
        n.max(tasks.len().max(((max - 1) * (n + 1) + cnt) as usize) as i32)
    }
}