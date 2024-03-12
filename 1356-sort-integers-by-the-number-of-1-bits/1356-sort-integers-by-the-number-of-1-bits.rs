impl Solution {
    pub fn sort_by_bits(arr: Vec<i32>) -> Vec<i32> {
        let mut arr = arr;
        arr.sort_by(|a, b| a.count_ones().cmp(&b.count_ones()).then(a.cmp(b)));
        arr
    }
}