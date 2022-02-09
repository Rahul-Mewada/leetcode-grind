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
    public int minDepth(TreeNode root) {
        Queue<TreeNode> nodes = new LinkedList<>();
        if(root == null) return 0;
        nodes.add(root);
        int minDepth = 0;
        
        while(!nodes.isEmpty()) {
            int size = nodes.size();
            minDepth++;
            while(size-- > 0) {
                TreeNode cur = nodes.poll();
                if(cur.left == null && cur.right == null) {
                    // this is a leaf node
                    return minDepth;
                }
                if(cur.left != null) nodes.add(cur.left);
                if(cur.right != null) nodes.add(cur.right);
            }   
        }
        
        
        return minDepth;
    }
    
}