use std::cmp::min;
impl Solution {
    pub fn find_min_arrow_shots(points: Vec<Vec<i32>>) -> i32 {
        let mut arr = points;
        arr.sort_unstable();
        let mut ans = 1;

        let mut num = arr[0][1];
        for i in 1..arr.len() {
            if arr[i][0] > num {
                ans += 1;
                num = arr[i][1];
            } else {
                num = min(arr[i][1], num);
            }
        }
        ans
    }
}