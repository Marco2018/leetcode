class Solution {
public:
    void dfs(int n, int m, int i, int j, vector<vector<int>>& path, vector<vector<int>>& visited, vector<vector<int>>& grid){
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int ii, jj;
        visited[i][j] = 1;
        path.push_back({i, j});
        for(auto dir:directions){
            ii = dir[0]; jj = dir[1];
            if(i+ii>=0 && i+ii<n && j+jj>=0 && j+jj<m){
                if(grid[i+ii][j+jj] == 1 && visited[i+ii][j+jj] == 0){
                    dfs(n, m, i+ii, j+jj, path, visited, grid);
                }
            }
        }
        return;
    }
    int largestIsland(vector<vector<int>>& grid) {
        if(grid.size() == 0) return 0;
        int n = grid.size(), m = grid[0].size();
        vector<vector <int> > visited(n, vector<int>(m,0));
        vector<vector <int> > dp(n, vector<int>(m,0));
        vector<vector <vector<int>>> position(n, vector<vector<int>>(m, vector<int> (2, -1)));
        int i, j;
        int num;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(grid[i][j] == 1 && visited[i][j] == 0){
                    vector<vector<int>> path;
                    dfs(n, m, i, j, path, visited, grid);
                    num = path.size();
                    for(auto pos:path){
                        dp[pos[0]][pos[1]] = num;
                        position[pos[0]][pos[1]] = {i, j};
                    }
                }
            }
        }
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int ii, jj, res = 0, temp;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(grid[i][j]==0){
                    temp = 1;
                    vector<vector<int>> temp_pos;
                    for(auto dir:directions){
                        ii = dir[0]; jj = dir[1];
                        if(i+ii>=0 && i+ii<n && j+jj>=0 && j+jj<m){
                            if(dp[i+ii][j+jj]!=0){
                                auto it = find(temp_pos.begin(), temp_pos.end(), position[i+ii][j+jj]);
                                if( it==temp_pos.end()){
                                    temp_pos.push_back(position[i+ii][j+jj]);
                                    temp += dp[i+ii][j+jj];
                                }
                            }
                        }
                    }
                    res = max(res, temp);
                }
                else{
                    res = max(res, dp[i][j]);
                }
            }
        }
        return res;        
    }
};