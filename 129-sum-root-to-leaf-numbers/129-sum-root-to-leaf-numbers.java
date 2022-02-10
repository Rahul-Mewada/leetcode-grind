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
    public int sumNumbers(TreeNode root) {
        if(root == null) return 0;
        return getPathSum(root, 0);
    }
    
    public int getPathSum(TreeNode root, int curPath) {
        String strPath = String.valueOf(curPath) + String.valueOf(root.val);
        curPath = Integer.parseInt(strPath);
        
        if(root.right == null && root.left == null) return curPath;
        
        int leftPath = 0;
        int rightPath = 0;
        
        if(root.left != null) leftPath = getPathSum(root.left, curPath);
        if(root.right != null) rightPath = getPathSum(root.right, curPath);
        
        
        return rightPath + leftPath;
    }
}