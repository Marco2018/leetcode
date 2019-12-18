class Solution {
public:
    int min_num = INT_MAX; 
    int distance(vector<int>& worker, vector<int>& bike){
        return abs(worker[0] - bike[0]) +  abs(worker[1] - bike[1]);
    }
    void dfs(int worker_index, vector<vector<int>>& workers, vector<vector<int>>& bikes, int sum_num, vector<int>& used){
        if(worker_index == workers.size()){
            min_num = min(min_num, sum_num);
            return;
        }
        if(sum_num > min_num) return;
        int i;
        for(i=0;i<bikes.size();i++){
            if(used[i] == 0){
                used[i] = 1;
                int d = distance(workers[worker_index], bikes[i]);
                dfs(worker_index + 1, workers, bikes, sum_num + d, used);
                used[i] = 0;
            }
        }
        return;
    }
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        int n = workers.size(), m = bikes.size();
        vector<int> used(m ,0);
        dfs(0, workers, bikes, 0, used);
        return min_num;
    }
};