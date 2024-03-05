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
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let (mut list1, mut list2) = (list1, list2);

        let mut head = Some(Box::new(ListNode::new(0)));
        let mut tail = &mut head;

        while list1.is_some() && list2.is_some() {
            let (val1, val2) = (list1.as_ref().unwrap().val, list2.as_ref().unwrap().val);

            if val1 < val2 {
                tail.as_mut().unwrap().next = list1;
                list1 = tail.as_mut().unwrap().next.as_mut().unwrap().next.take();
            } else {
                tail.as_mut().unwrap().next = list2;
                list2 = tail.as_mut().unwrap().next.as_mut().unwrap().next.take();
            }

            tail = &mut tail.as_mut().unwrap().next;
        }

        while list1.is_some() {
            tail.as_mut().unwrap().next = list1;
            list1 = tail.as_mut().unwrap().next.as_mut().unwrap().next.take();
            tail = &mut tail.as_mut().unwrap().next;
        }

        while list2.is_some() {
            tail.as_mut().unwrap().next = list2;
            list2 = tail.as_mut().unwrap().next.as_mut().unwrap().next.take();
            tail = &mut tail.as_mut().unwrap().next;
        }

        head.unwrap().next
    }
}