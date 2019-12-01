class Solution {
public:
    int check_left(int i, int j,vector<vector<int>>& matrix, int x){
        int a, res = 0;
        for(a=1;a<=x;a++){
            if(matrix[i-a][j] != 1)
                return res;
            else res += 1;
        }
        return res;
    }
    int check_top(int i, int j,vector<vector<int>>& matrix, int x){
        int a, res = 0;
        for(a=1;a<=x;a++){
            if(matrix[i][j-a] != 1)
                return res;
            else res += 1;
        }
        return res;
    }
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(); 
        if(m==0) return 0;
        int n = matrix[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        int i,j,res=0;
        for(i=1;i<=m;i++){
            for(j=1;j<=n;j++){
                if (matrix[i-1][j-1] == 1){
                    int x = dp[i-1][j-1];
                    int top = check_top(i-1,j-1,matrix,x);
                    int left = check_left(i-1,j-1,matrix,x);
                    dp[i][j] = min(top, left) + 1;
                    res += dp[i][j];
                }
            }
        }
        return res;
    }
};

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(); 
        if(m==0) return 0;
        int n = matrix[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        int i,j,res=0;
        for(i=1;i<=m;i++){
            for(j=1;j<=n;j++){
                if (matrix[i-1][j-1] == 1){
                    int x = min(dp[i-1][j], dp[i][j-1]);
                    if(matrix[i-1-x][j-1-x] == 1)
                        dp[i][j] = x+1;
                    else dp[i][j] = x;
                    res += dp[i][j];
                }
            }
        }
        return res;
    }
};