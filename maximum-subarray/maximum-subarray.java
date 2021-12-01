class Solution {
    public int maxSubArray(int[] nums) {
        int maxCurrent = nums[0];
        int maxGlobal = maxCurrent;
        
        
        for (int i = 1; i < nums.length; i++) {
            maxCurrent = Math.max(nums[i], nums[i] + maxCurrent);
            maxGlobal = Math.max(maxCurrent, maxGlobal);
        }
        
        return maxGlobal;
    }
}