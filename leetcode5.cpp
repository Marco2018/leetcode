class Solution {
public:
    string longestPalindrome(string s) {
        int n=s.size();
        if (n==0) return "";
        int res_length=1,res_left=0,start=0,pivot,left,right;
        while(start<n-1){
            pivot=start+1;
            while (pivot<n && s[pivot]==s[start]) pivot++;
            left=start-1;right=pivot;
            while (left>=0 && right<=n-1){
                if (s[left]==s[right]){
                    left--;right++;
                }
                else
                    break;
            }
            start=pivot;
            if (res_length<right-left-1){
                res_length=right-left-1;res_left=left+1;
            }
        }
        return s.substr(res_left,res_length);
    }
};

Runtime: 4 ms, faster than 99.88% of C++ online submissions for Longest Palindromic Substring.
Memory Usage: 8.9 MB, less than 99.30% of C++ online submissions for Longest Palindromic Substring