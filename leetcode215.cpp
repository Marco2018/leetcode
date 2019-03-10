#include <iostream>
#include <vector>
#include <queue>
using namespace std;
struct myCmp{
    bool operator ()(const int &a,const int &b){
        return a<b;
    }
};
class Solution {

public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,myCmp> num;
        int n =nums.size();
        for (int i=0;i<n;i++){
            num.push(nums[i]);
        }
        for (int i=0;i<k-1;i++){
            num.pop();
        }
        return num.top();
    }
};
int main() {
    vector<int> nums={2,3,1,5,4};
    Solution s;
    int k=2;
    printf("%d",s.findKthLargest(nums,k));
    return 0;
}
