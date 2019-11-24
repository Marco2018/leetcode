class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int n = distance.size();
        vector<int> accu(n+1, 0);
        for(auto i=1;i<n+1;i++){
            accu[i] = accu[i-1]+distance[i-1];
        }
        int clock_dis = abs(accu[destination]-accu[start]);
        int unclock_dis = accu[n]-clock_dis;
        return min(clock_dis, unclock_dis); 
    }
};