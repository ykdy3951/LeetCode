impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        strs.into_iter().reduce(|acc, cur| {
            acc.chars()
                .zip(cur.chars())
                .take_while(|(a,c)| a == c)
                .map(|(c,_)| c)
                .collect()
        }).unwrap()
    }
}