class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n=strs.size(),i,j;
        if(n==0 || strs[0].length()==0) return "";
        string res="";
        for (i=0;i<strs[0].length();i++){
            for (j=0;j<n;j++){
                if(strs[j].length()<i) return res;
                if(strs[j][i]!=strs[0][i]) return res;
            }
            res+=strs[0][i];
        }
        return res;
    }
};
两种情况：1.长度不够了 "fl" "flow"
2.字符不同
Runtime: 8 ms, faster than 94.25% of C++ online submissions for Longest Common Prefix.