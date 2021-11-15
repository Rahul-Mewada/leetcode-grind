/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> elements = new ArrayList();
        inorder(root, elements);
        return elements;
    }
    
    public void inorder(TreeNode root, List<Integer> elements) {
        if(root == null) {
            return;
        }
        
        inorder(root.left, elements);
        elements.add(root.val);
        inorder(root.right, elements);
        return;
    }
}