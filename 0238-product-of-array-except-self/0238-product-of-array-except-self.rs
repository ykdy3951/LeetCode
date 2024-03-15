impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut arr = vec![];
        let mut prefix = 1;
        for i in nums.clone() {
            arr.push(prefix);
            prefix *= i;
        }

        let mut postfix = 1;
        for i in (0..nums.len()).rev() {
            arr[i] *= postfix;
            postfix *= nums[i];
        }

        arr
    }
}