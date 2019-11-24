#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <bits/stdc++.h> 
using namespace std;
class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        vector<int> cnt(26, INT_MAX); //#include <bits/stdc++.h> 
		vector<string> res;
		for (auto s: A) {
			vector<int> cnt1(26, 0);
			for (auto c:s) ++cnt1[c-'a'];
			for(int i=0;i<26;i++) cnt[i] = min(cnt[i], cnt1[i]);
		}
		for(int i =0;i<26;i++){
			for(int j=0;i<cnt[i];j++){
				res.push_back(string(1, i + 'a'));
			}
		}
		return res;
    }
};
int main() {
	Solution s1;
	vector<string> A = {"bella","label","roller"};
	s1.commonChars(A);
	return 0;
}