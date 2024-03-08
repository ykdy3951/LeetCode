impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let mut carry = 0;
        
        let mut a = a.chars().collect::<Vec<char>>();
        let mut b = b.chars().collect::<Vec<char>>();

        let mut result = String::new();

        while !a.is_empty() || !b.is_empty() {
            let mut sum = carry;
            if let Some(digit) = a.pop() {
                sum += digit.to_digit(2).unwrap();
            }
            if let Some(digit) = b.pop() {
                sum += digit.to_digit(2).unwrap();
            }
            carry = sum / 2;
            result.push_str(&(sum % 2).to_string());
        }

        if carry > 0 {
            result.push_str(&carry.to_string());
        }

        result.chars().rev().collect()
    }
}