impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let ans = digits.iter().rev();
        let mut carry = 1;

        let mut result = Vec::new();
        for digit in ans {
            let sum = digit + carry;
            result.push(sum % 10);
            carry = sum / 10;
        }

        if carry > 0 {
            result.push(carry);
        }

        result.iter().rev().cloned().collect::<Vec<i32>>()
    }
}