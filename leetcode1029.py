class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        auto cmp=[](vector<int> &a, vector<int> &b){
            return a[0]-a[1]<b[0]-b[1];
        };
        int res = 0, n = costs.size();
        sort(costs.begin(), costs.end(), cmp);
        int i;
        for(i=0;i<n/2;i++) res+=costs[i][0];
        for(i=n/2;i<n;i++) res+=costs[i][1];
        return res;
    }
};