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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> allPaths = new ArrayList<>(new ArrayList<>());
        List<Integer> currentPath = new ArrayList<>();
        
        pathSum(root, targetSum, allPaths, currentPath);
        
        return allPaths;
    }
    
    public void pathSum(TreeNode root, int targetSum, List<List<Integer>> allPaths, List<Integer> currentPath) {
        if (root == null) {
            return;
        }
        System.out.print(root.val);
        
        targetSum -= root.val;
        currentPath.add(root.val);
        
        if(root.left == null && root.right == null && targetSum == 0) {
            allPaths.add(new ArrayList(currentPath));
        }
        
        if(root.left != null) {
            pathSum(root.left, targetSum, allPaths, currentPath);
            currentPath.remove(currentPath.size() - 1);
        }
        
        if(root.right != null) {
            pathSum(root.right, targetSum, allPaths, currentPath);
            currentPath.remove(currentPath.size() - 1);
        }
        
        return;
    }
}