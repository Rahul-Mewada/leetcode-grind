/*
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
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> averages = new ArrayList<>();
        Queue<TreeNode> bfsQ = new LinkedList<>();
        if(root != null) bfsQ.add(root);
        
        while(!bfsQ.isEmpty()){
            Double sum = 0.0;
            int count = 0;
            int size = bfsQ.size();
            
            while(size-- > 0) { 
                TreeNode cur = bfsQ.poll();
                sum += Double.valueOf(cur.val);
                count++;
                if(cur.left != null) bfsQ.add(cur.left);
                if(cur.right != null) bfsQ.add(cur.right);
            }
            
            averages.add(sum/count);
        }
        return averages;
    }
}
