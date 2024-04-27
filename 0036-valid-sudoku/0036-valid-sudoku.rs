use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut row = HashSet::new();
        let mut col = HashSet::new();
        let mut square = vec![HashSet::new(); 9];

        for i in 0..9 {
            for j in 0..9 {
                if let Some(val) = board[i][j].to_digit(10) {
                    if !row.insert((i, val)) {
                        return false;
                    }

                    if !col.insert((j, val)) {
                        return false;
                    }

                    if !square[3 * (i/3) + (j/3)].insert(val) {
                        return false;
                    }
                }
            }
        }

        true
    }
}