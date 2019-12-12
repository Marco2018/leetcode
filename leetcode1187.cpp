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
    //how many operations is needed
    int dp[2001][2001];
    int dfs(vector<int>& arr1, vector<int>& arr2, int index1, int index2, int prev){
        //prev 表示之前已经固定的元素中的最大值
        int r1, r2;
        
        if(index1>=arr1.size()) return 0; //finish
        //operation on arr1[index1]
        index2 = upper_bound(arr2.begin()+index2, arr2.end(), prev) - arr2.begin();
        if(dp[index1][index2]) return dp[index1][index2];

        if(index2>=arr2.size()) r1 = arr2.size()+1; //can not do opeartions
        else r1 = 1+dfs(arr1, arr2, index1+1, index2, arr2[index2]);
        //no opeartions
        if(prev<arr1[index1]) r2 = dfs(arr1, arr2, index1+1, index2, arr1[index1]);
        else r2 = arr2.size() + 1;
        
        dp[index1][index2] = min(r1, r2);
        return min(r1, r2);
    }
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        sort(arr2.begin(), arr2.end());
        auto res = 1;
        // auto res = dfs(arr1, arr2, 0, 0, -100000);
        if(res<=arr2.size()) return res;
        return -1;

    }
};                                                                                                                               
int main() {
	Solution s1;
    // cout<<s;
    vector<int> arr1 = {1,5,3,6,7};
    vector<int> arr2 = {1,3,2,4};
    int res = s1.makeArrayIncreasing(arr1, arr2);
    cout << res;
    system("pause");
	return 0;
}
