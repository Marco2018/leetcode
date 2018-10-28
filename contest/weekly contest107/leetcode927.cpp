#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include "time.h"
#include <numeric>
using namespace std;
class Solution {
public:
    vector<int> threeEqualParts(vector<int>& A) {
        vector<int> n1={-1,-1};
        vector<int> ones;
        int n =A.size(),count=0;
        for(int i=0;i<n;i++){
            if (A[i]==1){
                ones.push_back(i);count++;
            }
        }
        if (count%3!=0)
            return n1;
        if (count==0)
            return vector<int>{0,n-1};
        int number=count/3,right_zeros=0,right=n-1;
        while (right>=0) {
            if (A[right] == 0) {
                right--;
                right_zeros++;
            }
            else
                break;
        }
        vector<int> nums1(A.begin()+ones[0], A.begin() + ones[number-1]+1+right_zeros);
        vector<int> nums2(A.begin()+ones[number], A.begin() + ones[ones.size()-number-1]+1+right_zeros);
        vector<int> nums3(A.begin()+ones[ones.size()-number], A.end());
        if (nums1==nums2 && nums2==nums3){
            return vector<int>{ones[number-1]+right_zeros,ones[ones.size()-number-1]+1+right_zeros};
        }
        else
            return n1;
    }
};
int main() {
    Solution s=Solution();
    vector<int> A={1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0};
    vector<int> a;
    a=s.threeEqualParts(A);
    cout<<a[0]<<a[1];
    return 0;
}
