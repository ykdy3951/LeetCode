impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let mut pos = (0, 0);
        let sb = s.as_bytes();
        let mut len = 1;
        let mut vec = vec![vec![false; 1000]; 1000];

        for i in 0..s.len() {
            vec[i][i] = true;
        }

        for i in 0..(s.len()-1) {
            if sb[i] == sb[i+1] {
                vec[i][i+1] = true;
                if len < 2 {
                    pos = (i, i + 1);
                    len = 2;
                }
            }
        }

        for k in 2..s.len() {
            for i in 0..(s.len()-k) {
                let j = i + k;
                if (sb[i] == sb[j]) && (vec[i+1][j-1]) {
                    vec[i][j] = true;
                    if len < (j-i+1) {
                        len = j-i+1;
                        pos = (i, j);
                    }
                }
            }
        }

        s[pos.0..=pos.1].to_string()
    }
}