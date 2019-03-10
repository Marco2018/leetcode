#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int min(int a,int b){
        if (a>b) return b;
        else return a;
    }
    vector<int> shortestToChar(string S, char C) {
        int n=S.length();
        vector<int> nums(n,n);
        for(int i=0;i<n;i++){
            if (S[i]==C){
                nums[i]=0;
            }
            else{
                if(i!=0){
                    nums[i]=min(nums[i-1]+1,nums[i]);
                }
            }
        }
        for(int i=n-2;i>=0;i--){
            nums[i]=min(nums[i+1]+1,nums[i]);
        }
        return nums;
    }
};
int main() {
    string str="loveleetcode";
    char C='e';
    Solution s;
    s.shortestToChar(str,C);
    return 0;
}
