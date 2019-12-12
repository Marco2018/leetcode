class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        auto cmp = [](vector<int>& a, vector<int>& b){
            return a[0] < b[0];
        };
        sort(intervals.begin(), intervals.end(),cmp);
        vector<int> times;
        priority_queue<int, vector<int>, greater<int>> q(times.begin(),times.end());
        int count = 1;
        if(intervals.size()==0) return 0;
        q.emplace(INT_MIN);
        for (auto meet:intervals){
            int last_time = q.top();
            if(last_time<=meet[0]){
                q.pop();
                q.emplace(meet[1]);
            }
            else{
                count++;
                q.emplace(meet[1]);
            }
        }
        return count;
    }
};