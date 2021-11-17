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
    public TreeNode invertTree(TreeNode root) {
        dfs(root);
        return root;
    }
    
    public void dfs(TreeNode root) {
        if(root == null) return;
        
        TreeNode temp = root.right;
        root.right = root.left;
        root.left = temp;
        
        if(root.right != null) {
            dfs(root.right);
        }
        
        if(root.left != null){
            dfs(root.left);
        }
        
        return;
    }
} 