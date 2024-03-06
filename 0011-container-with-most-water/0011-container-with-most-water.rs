impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut max_area = 0;
        let (mut left, mut right) = (0, height.len() - 1);

        while left < right {
            let heigth = std::cmp::min(height[left], height[right]);
            max_area = std::cmp::max(max_area, (right - left) as i32 * heigth);

            while height[left] <= heigth && left < right {
                left += 1;
            }

            while height[right] <= heigth && left < right {
                right -= 1;
            }
        }

        max_area
    }
}