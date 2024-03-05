impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut ans = 0;
        let mut prev = 0;

        for &byte in s.as_bytes() {
            ans += match byte {
                b'I' => 1,
                b'V' if prev == b'I' => 3,
                b'V' => 5,
                b'X' if prev == b'I' => 8,
                b'X' => 10,
                b'L' if prev == b'X' => 30,
                b'L' => 50,
                b'C' if prev == b'X' => 80,
                b'C' => 100,
                b'D' if prev == b'C' => 300,
                b'D' => 500,
                b'M' if prev == b'C' => 800,
                b'M' => 1000,
                _ => unsafe { std::hint::unreachable_unchecked() }
            };
            prev = byte;
        }

        ans
    }
}