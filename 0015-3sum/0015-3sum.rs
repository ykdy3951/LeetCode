use std::collections::HashSet;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: HashSet<Vec<i32>> = HashSet::new();
        let mut nums = nums;
        nums.sort();

        for i in 0..(nums.len() - 2) {
            let n1 = nums[i];
            let (mut j, mut k) = (i + 1, nums.len() - 1);

            while j < k {
                let n2 = nums[j];
                let n3 = nums[k];

                let tmp = n1 + n2 + n3;

                if tmp > 0 {
                    k -= 1;
                } else if tmp < 0 {
                    j += 1;
                } else {
                    result.insert(vec![n1, n2, n3]);

                    while j < k && nums[j] == n2 {
                        j += 1;
                    }

                    while j < k && nums[k] == n3 {
                        k -= 1;
                    }
                }
            }

        }

        result.into_iter().collect::<Vec<Vec<i32>>>()
    }
}