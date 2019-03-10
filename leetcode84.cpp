#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int largestRectangleArea(vector<int>& nums) {
        int n=nums.size(),ans=0;
        int width,height;
        for (int i=0;i<n;i++){
            height=nums[i];
            if(i >= 1 && nums[i] <= nums[i-1])
                continue;//减枝
            for(int j=i;j<n;j++){
                width=j-i+1;
                height=min(height,nums[j]);
                ans=max(ans,width*height);
            }
        }
        return ans;
    }
};
int main() {
    vector<int> nums={2,1,5,6,2,3};
    Solution s;
    printf("%d",s.largestRectangleArea(nums));
    return 0;
}
