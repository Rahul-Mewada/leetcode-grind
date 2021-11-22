class Solution {
    public int uniquePaths(int m, int n) {
        int[][] data = new int[m][n];
        return dfs(0,0,m-1,n-1,data);
    }
    
    public int dfs(int curM, int curN, int m, int n, int[][] data) {
        if(curM > m || curN > n) {
            return 0;
        }
        
        if(curM == m && curN == n) {
            return 1;
        }
        
        if(data[curM][curN] == 0) {
            int down = dfs(curM + 1, curN, m, n, data);
            int right = dfs(curM, curN+1, m, n, data);
            data[curM][curN] = down + right;
        } 
        
        return data[curM][curN];
    }
    
}