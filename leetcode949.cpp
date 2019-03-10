#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<sstream>
using namespace std;
class Solution {
public:
	string largestTimeFromDigits(vector<int>& A) {
		sort(A.begin(), A.end());
		stringstream ss;
		string str1;
		int ans = -1;
		do{
			int h = A[0] * 10 + A[1];
			int m = A[2] * 10 + A[3];
			if (h >= 24 || m >= 60) continue;
			if (h * 60 + m > ans) {
				ans = h * 60+m;
				ss.str("");
				ss << A[0] << A[1] << ":" << A[2] << A[3];
			}
		} while (next_permutation(A.begin(), A.end()));
		str1 = ss.str();
		return str1;
	}
};
int main() {
	Solution s1 = Solution();
	vector<int> nums = { 1,4,5,5 };
	string str1 = s1.largestTimeFromDigits(nums);
	printf("%s", str1.c_str());
	system("pause");
	return 0;
}