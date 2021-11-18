/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return dfs(root, p.val, q.val);
    }
    
    public TreeNode dfs(TreeNode root, int p, int q) {
        if(root == null) {
            return null;
        }

        TreeNode left = null;
        TreeNode right = null;

        
        if(root.val == p || root.val == q) {
            return root;
        }

        left = dfs(root.left, p, q);
        right = dfs(root.right, p, q);
        
        if(left != null && right != null) {
            return root;
        } else if (left != null) {
            return left;
        } else if (right != null) {
            return right;
        }
        
        return null;
    }
}