class Solution {
public:
    int subarrayBitwiseORs(vector<int>& A) {
       unordered_set<int> res;
       unordered_map<pair<int, int>, int> memo;
       int n = A.size();
       int i = 0, length, ans;
       for(i=0;i<n;i++){
           res.insert(A[i]);
           memo[pair(i, i+1)] = A[i];
       }
       for(length=2;length<=n;length++){
           for(i=0;i<=n-length;i++){
               ans = memo[pair(i, i+length-1)] | A[i+length-1];
               memo[pair(i, i + length)] = ans;
               res.insert(ans);
           }
       } 
       return res.size();
    }
};