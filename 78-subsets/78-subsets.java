class Solution {
    // [1, 2, 3]
    // []
    // [] [1]
    // [] [2] [1] [1, 2]
    // [] [3] [2] [2,3] [1] [1, 3] [1, 2] [1, 2, 3]
    
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<List<Integer>>();
        List<Integer> curSubset = new ArrayList<>();
        populateSubsets(nums, 0, subsets, curSubset);
        
        return subsets;
    }
    
    public void populateSubsets(int[] nums, int index, List<List<Integer>> subsets, List<Integer> curSubset) {
        if(index > nums.length - 1) {
            subsets.add(curSubset);
            return;
        }
        
        int num = nums[index];
        List<Integer> newList = new ArrayList<>(curSubset);
        newList.add(num);
        
        populateSubsets(nums, index+1, subsets, new ArrayList<>(curSubset));
        populateSubsets(nums, index+1, subsets, newList);
        
        return;
    }
}