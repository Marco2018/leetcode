class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int res = 0, n = points.size();
        if(n<=1) return 0;
        int last_x = points[0][0], last_y = points[0][1],x,y;
        for(int i=1;i<n;i++){
            //cout<<last_x<<" "<<last_y<<" ";
            x = points[i][0]; y = points[i][1];
            // cout<<x<<" "<<y<<" ";
            res += max(abs(last_x-x), abs(last_y-y));
            last_x = x;
            last_y = y;
        }
        return res;
    }
};