use std::cmp;
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut arr = vec![2147483647; cost.len()];
        arr[0] = cost[0];
        arr[1] = cost[1];
        for i in 2..arr.len() {
            arr[i] = cmp::min(arr[i-1], arr[i-2]) + cost[i];
        }
        cmp::min(arr[arr.len()-1], arr[arr.len()-2])
    }
}