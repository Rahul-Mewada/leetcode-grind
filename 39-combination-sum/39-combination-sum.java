class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        List<Integer> curComb = new ArrayList<Integer>();
        Arrays.sort(candidates);
        generateCombinations(candidates, target, 0, results, curComb, 0);
        return results;
    }
    
    public int generateCombinations(int[] nums, int target, int i, List<List<Integer>> results, List<Integer> curComb, int curSum) {
        if(i >= nums.length || curSum > target) return -1;
        if(curSum == target) {
            results.add(new ArrayList<>(curComb));
            return -1;
        }
        
        List<Integer> curInstance = new ArrayList<>(curComb);
        
        for(int j = i; j < nums.length; j++) {
            curInstance.add(nums[j]);
            int res = this.generateCombinations(nums, target, j, results, curInstance, curSum + nums[j]);
            curInstance.remove(curInstance.size() - 1);
            if(res == -1) break;
        }
        
        return curSum;
    }
}