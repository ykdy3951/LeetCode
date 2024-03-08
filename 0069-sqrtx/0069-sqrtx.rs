impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if x == 0 {
            return 0;
        }
        else if x <= 3 {
            return 1;
        }

        let (mut low, mut high) = (2, 46340.min(x/2));

        if high * high <= x {
            return high;
        }

        while low + 1 < high {
            let mid = (low + high) / 2;
            let pow_mid = mid * mid;

            if pow_mid == x {
                return mid;
            }
            else if pow_mid > x {
                high = mid;
            }
            else {
                low = mid;
            }
        }

        low
    }
}