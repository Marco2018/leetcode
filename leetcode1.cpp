#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;
class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int, int> map1;
		unordered_map<int, int>::iterator it;
		int i,n = nums.size();
		for (i = 0;i < n;i++) {
			it = map1.find(target-nums[i]);
			if (it != map1.end()) {
				vector<int> res{ it->second ,i };
				return res;
			}
			else {
				map1[nums[i]] = i;
			}
		}
	}
};
int main() {
	int target = 8;
	vector<int> nums = { 4,4,3,15 };
	Solution s1;
	vector<int> res;
	res=s1.twoSum(nums, target);
	cout << res[0] << " " << res[1];
	system("pause");
	return 0;
}