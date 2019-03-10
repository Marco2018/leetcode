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
bool cmp1(string& a, string& b) {
	int i;
	for (i = 0; i < min(a.size(), b.size()); i++) {
		if (a[i] != b[i])
			return map1[a[i]] < map1[b[i]];
	}
	return a.size() < b.size();
}
class Solution {
public:
	bool isAlienSorted(vector<string>& words, string order) {
		vector<string> words2 = words;
		if (words.size() == 0) return true;
		int n = order.size(), i, j;
		for (i = 0; i < n; i++) {
			map1[order[i]] = i;
		}
		sort(words.begin(), words.end(), cmp1);
		for (i = 0; i < words.size(); i++) {
			if (words2[i] != words[i])
				return false;
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