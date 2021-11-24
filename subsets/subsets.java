class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        
        subsets(nums, 0, results, cur);
        return results;
    }
    
    public void subsets(int[] nums, int index, List<List<Integer>> results, List<Integer> cur) {
        System.out.println(index);
        if(index >= nums.length) {
            results.add(cur);
            return;
        }
        
        List<Integer> temp = new ArrayList(cur);
        List<Integer> tempOne = new ArrayList(cur);
        tempOne.add(nums[index]);
        subsets(nums, index+1, results, temp);
        subsets(nums, index+1, results, tempOne);
        return;
    }
}