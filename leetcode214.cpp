#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<sstream>
#include <typeinfo>
#include<map>
using namespace std;
const int maxn = 5000;
bool ispalin(string s) {
	int n = s.size();
	int left, right;
	if (n % 2 == 1) {
		left = right = n / 2;
		while (left >= 0 && right < n) {
			if (s[left] != s[right]) {
				return false;
			}
			left--;
			right++;
		}
		return true;
	}
	else {
		left = n / 2 - 1;
		right = n / 2;
		while (left >= 0 && right < n) {
			if (s[left] != s[right]) {
				return false;
			}
			left--;
			right++;
		}
		return true;
	}
}
class Solution {
public:
	string shortestPalindrome(string s) {
		string s_temp = s;
		reverse(s_temp.begin(), s_temp.end());
		int n = s.size(),i;
		if (ispalin(s)) return s;
		for (i = 1; i < n; i++) {
			if (ispalin(s_temp.substr(0, i) + s))
				return s_temp.substr(0, i) + s;
			//if (ispalin(s + s_temp.substr(n - i, n)))
				//return s + s_temp.substr(n - i, n);
		}
	}
};
int main() {
	vector<int> nums = { 1, 2, 3, 4, 5, 6 };
	Solution s = Solution();
	int res;
	string s1 = "dedcba",s2,s3;
	//reverse(s1.begin(), s1.end());
	//cout << "s1" << s1;
	s3 = s1.substr(0, 3) + "123";
	s2 = s.shortestPalindrome(s1);
	cout << s2;
	system("pause");
	return 0;
}