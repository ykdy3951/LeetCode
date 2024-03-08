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
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut node = head;

        let mut val = -101;

        let mut head = Some(Box::new(ListNode::new(0)));
        let mut tail = &mut head;

        if node.is_none() {
            return None;
        }

        while node.is_some() {
            if node.as_ref().unwrap().val != val {
                val = node.as_ref().unwrap().val;
                *tail = Some(Box::new(ListNode::new(val)));
                tail = &mut tail.as_mut().unwrap().next;
            }
            node = node.take().unwrap().next;
        }

        head
    }
}