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

//                                                  5
//                                        4                     8
//                                  11                    13           4
//                              7       2                           5        1
// [[]]
// [5, 4] 17
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        dfs(root, targetSum, results, new ArrayList<Integer>());
        return results;  
    }
    
    
    public void dfs(TreeNode root, int sum, List<List<Integer>> results, List<Integer> curPath) {
        if(root == null) return;
        curPath.add(root.val);
        
        if(root.left == null && root.right == null) {
            if(sum == root.val) results.add(curPath);
            return;
        }
        
        dfs(root.left, sum - root.val, results, new ArrayList<>(curPath));
        dfs(root.right, sum - root.val, results, new ArrayList<>(curPath));
        
        curPath.remove(curPath.size() - 1);
        return;
    }
}