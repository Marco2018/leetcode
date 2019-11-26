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
   int nthUglyNumber(int k, int A, int B, int C) {
        int lo = 1, hi = 2 * (int) 1e9;
        int ab = A * B / __gcd(A, B);
        int bc = B * C / __gcd(B, C);
        int ac = A * C / __gcd(A, C);
        int abc = A * bc / __gcd(A, bc);
        while(lo < hi) {
            int mid = lo + (hi - lo)/2;
            int cnt = mid/A + mid/B + mid/C - mid/ab - mid/bc - mid/ac + mid/abc;
            if(cnt < k) 
                lo = mid + 1;
            else
			   //the condition: F(N) >= k
                hi = mid;
        }
        return lo;
    }
};
int main() {
	Solution s1;
    vector<vector<int>> points = {{3,4},{2,3},{1,2}};
    s1.nthUglyNumber(3,2,3,5);
    system("pause");
	return 0;
}