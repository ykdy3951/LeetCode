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
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = head;
        let mut node = &head;
        let mut len: i32 = 0;
        let mut count: i32 = 0;

        while let Some(n) = node {
            len += 1;
            node = &n.next;
        }
        
        let mut node = &mut head;
        while let Some(n) = node {
            if count == len / 2 {
                return Some(n.clone());
            }
            count += 1;
            node = &mut n.next;
        }

        None
    }
}