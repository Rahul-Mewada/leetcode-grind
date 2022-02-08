import java.util.*;;
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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> results = new LinkedList<List<Integer>>();
        Queue<TreeNode> bfsQ = new LinkedList<>();
        if(root != null) bfsQ.add(root);
        
        while(!bfsQ.isEmpty()) {
            List<Integer> result = new ArrayList<>();
            int size = bfsQ.size();
            
            while(size-- > 0) {
                TreeNode curNode = bfsQ.poll();
                result.add(curNode.val);
                if(curNode.left != null) bfsQ.add(curNode.left);
                if(curNode.right != null) bfsQ.add(curNode.right);
            }
            
            results.add(0, result);
        }
        
        return results;
    }
    
    
}