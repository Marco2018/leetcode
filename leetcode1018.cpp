class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& A) {
        int n = A.size(), temp = 0;
        vector<bool> res;
        for(int i=0;i<n;i++){
            temp = (2*temp+A[i])%5;
            if (temp%5==0) res.push_back(true);
            else res.push_back(false);
        }
        return res;
    }
};