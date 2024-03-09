// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;

fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>, ans: &mut Vec<i32>) {
    if let Some(tmp) = root {
        inorder_traversal(tmp.borrow().left.clone(), ans);
        ans.push(tmp.borrow().val);
        inorder_traversal(tmp.borrow().right.clone(), ans);
    }
}

impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut ans = Vec::new();
        inorder_traversal(root, &mut ans);
        ans
    }
}