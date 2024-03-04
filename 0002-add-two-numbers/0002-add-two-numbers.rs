impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut carry = 0;

        let mut head = Some(Box::new(ListNode::new(0)));
        let mut tail = head.as_mut();
        let (mut l1, mut l2) = (l1.as_ref(), l2.as_ref());
        let mut sum = 0;

        while l1.is_some() || l2.is_some() || carry > 0 {
            sum = carry;
            if let Some(node) = l1 {
                sum += node.val;
                l1 = node.next.as_ref();
            }
            if let Some(node) = l2 {
                sum += node.val;
                l2 = node.next.as_ref();
            }

            carry = sum / 10;
            let node = Some(Box::new(ListNode::new(sum % 10)));
            tail.as_mut().unwrap().next = node;
            tail = tail.unwrap().next.as_mut();
        }

        head.unwrap().next
    }
}