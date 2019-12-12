class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        auto cmp = [](vector<int>& a, vector<int>& b){
            return a[0] < b[0];
        };
        sort(intervals.begin(), intervals.end(),cmp);
        int end_time = INT_MIN;
        for (auto meet:intervals){
            if(meet[0]>=end_time){
                end_time = meet[1];
            }
            else{
                return false;
            }
        }
        return true;
    }
};