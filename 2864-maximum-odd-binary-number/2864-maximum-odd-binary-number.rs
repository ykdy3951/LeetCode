impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let mut arr = vec![0;2];
        for i in s.chars() {
            arr[i.to_digit(10).unwrap() as usize] += 1;
        }        

        let mut result = String::new();
        for _ in 0..(arr[1]-1) {
            result.push('1');
        }
        for _ in 0..arr[0] {
            result.push('0');
        }
        result.push('1');

        result
    }
}