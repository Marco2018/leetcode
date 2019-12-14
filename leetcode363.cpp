class Solution {
public:
    int get_maxsum_lower(vector<int> sums, int k){
        // Find the max subarray no more than K 
        set<int> accuSet;
        accuSet.insert(0);
        int curSum = 0, curMax = INT_MIN;
        for(int sum : sums) {
            curSum += sum;
            set<int>::iterator it = accuSet.lower_bound(curSum - k);
            if (it != accuSet.end()) curMax = max(curMax, curSum - *it);
                accuSet.insert(curSum);
        }
        return curMax;
    }
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        if (matrix.empty()) return 0;
        int n = matrix.size(), m = matrix[0].size(), res = INT_MIN;
        for (int left = 0; left < m; ++left) {
            vector<int> sums(n, 0);
            for (int right = left; right < m; ++right) {
                for (int i = 0; i < n; ++i) {
                    sums[i] += matrix[i][right];
                }
                int curMax = get_maxsum_lower(sums, k);
                res = max(res, curMax);
            }
        }
        return res;
    }
};