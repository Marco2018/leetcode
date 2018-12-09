#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<sstream>
#include <typeinfo>
#include<map>
using namespace std;
map<char, int> map1;
bool cmp1(int& a, int& b) {
	if (abs(a) != abs(b))
		return abs(a) < abs(b);
	return a < b;
}
class Solution {
public:
	bool canReorderDoubled(vector<int>& A) {
		map<int, int> map1;
		int i;
		for (i = 0; i < A.size(); i++) {
			map1[A[i]]++;
		}
		sort(A.begin(), A.end(), cmp1);
		for (i = 0; i < A.size(); i++) {
			if (map1[A[i]] == 0) continue;
			if (map1[2 * A[i]] < map1[A[i]]) return false;
			map1[2 * A[i]] -= map1[A[i]];
			map1[A[i]] = 0;
		}
		return true;
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