#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<sstream>
#include <typeinfo>
#include<map>
using namespace std;
int issorted(vector<string>& str) {
	int j;
	for (j = 1; j < str.size(); j++) {
		if (str[j - 1] > str[j]) return -1;
	}
	for (j = 1; j < str.size(); j++) {
		if (str[j - 1] == str[j]) return 0;
	}
	return 1;
}
class Solution {
public:
	int minDeletionSize(vector<string>& A) {
		int i, j, n = A.size();
		bool flag = true;
		vector<string> str(n, "");
		vector<string> str2(n, "");
		int count = 0;
		if (n <= 1) return count;
		for (i = 0; i < A[0].size(); i++) {
			for (j = 0; j < A.size(); j++) {
				str2[j] += A[j][i];
			}
			int res = issorted(str2);
			if (res == 1)
				return count;
			else {
				if (res == 0) {
					str = str2;
				}
				else {
					str2 = str;
					count++;
				}
			}
		}
		return count;
	}
};
int main() {
	vector<string> nums = { "ousnatait", "xzswvwztr", "luknznxob" };
	Solution s1 = Solution();
	int i;
	int res;
	if ("xg" < "yb")
		int a = 1;
	res = s1.minDeletionSize(nums);
	cout << res;
	system("pause");
	return 0;
}