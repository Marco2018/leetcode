#include <iostream>
#include <array>
#include <vector>
using namespace std;
class Solution {
public:
	vector<int> productExceptSelf(vector<int>& nums) {
		vector<int> zeros;
		long number = 1;
		int n = nums.size(),i;
		for (i = 0;i < n;i++) {
			if (nums[i] == 0) zeros.push_back(i);
		}
		if (zeros.size() >= 2) {
			vector<int> res(n,0);
			return res;
		}
		else if (zeros.size() == 1) {
			for (i = 0;i < n;i++) {
				if (i == zeros[0])
					continue;
				number *= nums[i];
			}
			vector<int> res(n, 0);
			res[zeros[0]] = number;
			return res;
		}
		else {
			for (i = 0;i < n;i++) {
				number *= nums[i];
			}
			vector<int> res(n);
			for (i = 0;i < n;i++) {
				res[i] = int(number / nums[i]);
			}
			return res;
		}
	}
};
int main() {
	Solution s1;
	vector <int> nums = { 0,0 };
	vector <int> res = s1.productExceptSelf(nums);
	for (int i = 0;i < nums.size();i++) {
		cout << res[i] << " ";
	}
	system("pause");
	return 0;
}