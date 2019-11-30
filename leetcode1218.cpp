class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        int n = arr.size(), res = 1;
        map<int, int> map1;
        if(n<=1) return n;
        for(auto num: arr){
            auto it = map1.find(num - difference);
            if(it!=map1.end()){
                map1[num] = map1[num-difference]+1;
                res = max(res, map1[num]);
            }
            else{
                map1[num] = 1;
            }
        }
        return res;
    }
}; 