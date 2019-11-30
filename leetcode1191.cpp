#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <bits/stdc++.h>
#include <map>
using namespace std;
class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        int n = arr.size(), i;
        long long sum1=0, left=0, right = 0, temp=0, left_temp=0, right_temp=0;
        long long res;
        long long sig_sum = 0;
        for(i=0;i<n;i++){
            temp+=arr[i];
            if(temp<0)temp=0;
            if(temp>sig_sum){
                sig_sum = temp;
            }
        }
        sig_sum = sig_sum%1000000007;
        for(i=0;i<n;i++){
            left_temp+=arr[i];
            sum1 += arr[i];
            if(left_temp>left){
                left = left_temp;
            }
        }
        for(i=n-1;i>=0;i--){
            right_temp+=arr[i];
            if(right_temp>right){
                right = right_temp;
            }
        }
        sum1 = sum1%1000000007; left = left%1000000007; right = right%1000000007;
        if(sum1>=0){
            if(k>=2) res = (k*sum1 + max((long long)0, right-sum1) + max((long long)0, left-sum1))%1000000007;
            else{
                int bigger = max(right, left);
                res = (k*sum1 + max(0, bigger))%1000000007;
            }
        }
        else{
            
            res = (max((long long)0, right) + max((long long)0, left))%1000000007;
        }
        return max(res, sig_sum);
    }
};                                                                                                                                             
int main() {
	Solution s1;
    double s =1.0*1/3;
    // cout<<s;
    vector<int> arr = {1,-2,1};
    int k = 5;
    int res = s1.kConcatenationMaxSum(arr, k);
    cout<<res;
    system("pause");
	return 0;
}
