// [-7,-3,2,3,11]
// [49, 9, 4, 9, 121]
//.  l        r
//. [n, n, n, n, 121]

class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        int left = 0;
        int right = nums.length - 1;
        int i = nums.length - 1;
        while(left <= right) {
            int leftSq = nums[left] * nums[left];
            int rightSq = nums[right] * nums[right];
            
            if(leftSq >= rightSq) {
                result[i] = leftSq;
                left += 1;
            } else {
                result[i] = rightSq;
                right -= 1;
            }
            
            i--;
        }
        return result;
    }
}