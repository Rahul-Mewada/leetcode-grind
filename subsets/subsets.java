class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subset = new ArrayList<>();
        subsets(nums, subset, 0, new ArrayList<>());
        return subset;
    }
    
    
    /*
    [1, 2, 3]
        i  I      
    
    []
    
    
    
    [
    [],
    [1],
    [1,2],
    [1,2,3],
    [1,3],
    [2],
    [2,3],
    
    ]
    */
    
    
    public void subsets(int[] nums, List<List<Integer>> subset, int index, List<Integer> current) {
        
        List<Integer> temp = new ArrayList<>(current);
        subset.add(temp);
        
        for(int i = index; i < nums.length; i++) {
            temp.add(nums[i]);
            subsets(nums, subset, i+1, temp);
            temp.remove(temp.size() - 1);
        }
        
        return;
    }
}