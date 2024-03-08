impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut arr = vec![0; n as usize + 1];
        arr[0] = 1;
        arr[1] = 1;

        for i in 2..=n as usize {
            arr[i] = arr[i - 1] + arr[i - 2];
        }

        arr[n as usize] as i32
    }
}