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

/*
                    2
             9             20
        1       2      3        4       
        
    
    [[3], [], []]
    [9, 20, 1, 2, 3, 4]
    [4, 3, 2, 1]
*/

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        boolean isLeftToRight = true;
        Queue<TreeNode> bfsQ = new LinkedList<>();
        
        if(root != null) bfsQ.add(root);
        
        while(!bfsQ.isEmpty()) {
            List<Integer> result = new LinkedList<>();
            int size = bfsQ.size();
            Queue<TreeNode> curLevel = new LinkedList<>();
            while(size-- > 0) {
                TreeNode cur = bfsQ.poll();
                if(isLeftToRight) {
                    result.add(cur.val);
                } else {
                    result.add(0, cur.val);
                }
                
                if(cur.left != null) bfsQ.add(cur.left);
                if(cur.right != null) bfsQ.add(cur.right);
            }
            
            isLeftToRight = !isLeftToRight;
            results.add(result);
        }
        
        return results;
    }
}