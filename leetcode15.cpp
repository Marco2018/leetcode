#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <set>
using namespace std;
struct VectorHash {
	size_t operator()(const std::vector<int>& v) const {
		std::hash<int> hasher;
		size_t seed = 0;
		for (int i : v) {
			seed ^= hasher(i) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
		}
		return seed;
	}
};
class Solution {
public:
	vector<vector<int>> threeSum(vector<int>& nums) {
		vector<vector<int>> res;
		unordered_set<vector<int>,VectorHash> s1;
		int i, n = nums.size();
		int j, k, sum1;
		sort(nums.begin(), nums.end());
		if (n < 3)return res;
		for (i = 0;i < n - 2;i++) {
			j = i + 1;k = n - 1;
			while (j < k) {
				sum1 = nums[i] + nums[j] + nums[k];
				if (sum1 == 0) {
					vector<int> temp{ nums[i],nums[j],nums[k] };
					if (true) {
						s1.insert(temp);
						res.push_back(temp);
					}
					j++;k--;
				}
				else if (sum1 < 0)
					j++;
				else
					k--;
			}
		}
		return res;
	}
};
int main() {
	vector<int> nums = { -1,0,1,2,-1,-4 };
	Solution s1;
	vector<int> res;
	s1.threeSum(nums);
	system("pause");
	return 0;
}