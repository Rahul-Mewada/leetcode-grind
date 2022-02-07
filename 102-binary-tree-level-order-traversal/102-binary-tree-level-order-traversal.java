import java.util.List;
import java.util.LinkedList;
import java.util.Queue;
import java.util.ArrayList;
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

// bfsQ =  [15, 7]
// level = 2
// result = [9, 20]
// results = [[3], [9, 20]]

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root != null) {
            return bfs(root);
        } else {
            return new ArrayList<>();
        }
    }
    
    public List<List<Integer>> bfs(TreeNode root) {
        List<List<Integer>> results = new ArrayList<>();
        Queue<TreeNode> bfsQ = new LinkedList<>();
        bfsQ.add(root);
        
        while(!bfsQ.isEmpty()) {
            int level = bfsQ.size();
            List<Integer> result = new ArrayList<>();
            while(level > 0) {
                level--;
                TreeNode cur = bfsQ.poll();
                result.add(cur.val);
                if(cur.left != null) bfsQ.add(cur.left);
                if(cur.right != null) bfsQ.add(cur.right);
            }
            results.add(result);
        }
        
        return results;
    }
}