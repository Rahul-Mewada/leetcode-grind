class Solution {
    public int climbStairs(int n) {
        int [] data = new int[n+1];
        return numWays(n, data);
    }
    
    public int numWays(int n, int[] data) {
        if(n == 0) {
            return 1;
        } else if (n < 0) {
            return 0;
        }
        
        if (data[n] == 0) {
            int oneStep = numWays(n-1, data);
            int twoStep = numWays(n-2, data);
            data[n] = (oneStep + twoStep);
        }
        
        return data[n];
    }
}