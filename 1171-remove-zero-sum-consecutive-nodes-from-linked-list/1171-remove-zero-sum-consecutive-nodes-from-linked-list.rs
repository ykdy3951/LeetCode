// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn remove_zero_sum_sublists(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let head = head;
        let mut tail = &head;
        let mut arr = Vec::new();
        
        let mut ans_head = Some(Box::new(ListNode::new(0)));
        let mut ans_tail = &mut ans_head;

        while let Some(node) = tail {
            arr.push(node.val);
            tail = &node.next;
        }

        let mut start = 0;

        while start < arr.len() {
            let mut sum = 0;
            let mut end = start;
            while end < arr.len() {
                sum += arr[end];
                if sum == 0 {
                    arr.drain(start..=end);
                    start -= 1;
                    break;
                }
                end += 1;
            }
            start += 1;
        }

        for i in arr {
            ans_tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(i)));
            ans_tail = &mut ans_tail.as_mut().unwrap().next;
        }
        
        ans_head.unwrap().next
    }
}