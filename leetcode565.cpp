#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n=nums.size();
        int tmp,ans=0;
        bool isvisited[n];
        fill(isvisited, isvisited + n, false);
        for (int i=0;i<n;i++){
            tmp=0;
            int item=nums[i];
            isvisited[i]= true;
            tmp++;
            while (!isvisited[item]){
                isvisited[item]= true;
                item=nums[item];
                tmp++;
            }
            ans=max(tmp,ans);
        }
        return ans;
    }
};
int main() {
    vector<int> nums={5,4,0,3,1,6,2};
    Solution s;
    printf("%d",s.arrayNesting(nums));
    return 0;
}
