impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        if row_index == 0 {
            return vec![1;1]
        }
        let mut arr = vec![1;2];
        for i in 1..row_index {
            let mut tmp = vec![1;1];
            for j in 1..arr.len() {
                tmp.push(arr[j] + arr[j-1]);
            }
            tmp.push(1);
            arr = tmp;
        }

        arr
    }
}