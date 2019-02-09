#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm> 
#include <string>

using namespace std;
class Solution {
public:
	vector<int> advantageCount(vector<int>& A, vector<int>& B) {
		vector<int> res;
		vector<int>::iterator pos;
		int i, n = A.size();
		sort(A.begin(), A.end());
		for (i = 0; i < n; i++) {
			pos = upper_bound(A.begin(), A.end(), B[i]);
			if (pos == A.end()) {
				res.push_back(*A.begin());
				A.erase(A.begin());
			}
			else {
				res.push_back(*pos);
				A.erase(pos);
			}
		}
		return res;
	}
};
int main() {
	Solution s1;
	vector<int> A = { 2,7,11,15 };
	vector<int> B = { 1,10,4,11 };
	s1.advantageCount(A, B);
	//cout << res;
	system("pause");
	return 0;
}