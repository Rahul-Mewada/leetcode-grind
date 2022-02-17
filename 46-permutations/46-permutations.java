/*


*/


class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        List<Integer> curPerm = new ArrayList<>();
        HashSet<Integer> remNums = new HashSet<Integer>();
        for(int ele : nums) remNums.add(ele);
        
        generatePermutations(nums, remNums, results, curPerm);
        
        return results;
        
    }
    
    public void generatePermutations(int[] nums, HashSet<Integer> remNums, List<List<Integer>> results, List<Integer> curPerm) {
        if(curPerm.size() == nums.length) {
            results.add(new ArrayList<Integer>(curPerm));
            return;
        }
        
        HashSet<Integer> newRemNums = new HashSet<>(remNums);
        
        for(int ele : remNums) {
            curPerm.add(ele);
            newRemNums.remove(ele);
            generatePermutations(nums, newRemNums, results, curPerm);
            curPerm.remove(curPerm.size() - 1);
            newRemNums.add(ele);
        }
        
        return;
    }
}