impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let target = (n * n + n) / 2;
        if n == 1 {
            return 1;
        }
        let (mut low, mut high) = (2, 707.min(target/2));
        if high * high == target {
            return high;
        }

        while low + 1 < high {
            let mid = (low + high) / 2;
            let pow_mid = mid * mid;

            if pow_mid == target {
                return mid;
            }
            else if pow_mid > target {
                high = mid;
            }
            else {
                low = mid;
            }
        }
        -1
    }
}