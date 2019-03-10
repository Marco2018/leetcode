#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<sstream>
using namespace std;
class Solution {
public:
	vector<double> medianSlidingWindow(vector<int>& nums, int k) {
		multiset<int> window (nums.begin(),nums.begin()+k);
		multiset<int> ::iterator median= window.begin();
		int i;
		for (i = 0; i < k / 2; i++) {
			median++;
		}
		vector<double> res;
		double temp;
		multiset<int>::iterator it;
		for (i = k; i < nums.size(); i++) {
			if (k % 2 == 1)
				res.push_back(*median);
			else {
				int prev = *(--median); median++;
				if (prev > 0 && *median > 0 || prev < 0 && *median < 0) {
					temp = *median*1.0 + (-*median + prev)*1.0 / 2;
					
				}
				else {
					temp = (*median + prev)*1.0 / 2;
				}
				res.push_back(temp);
			}
			window.insert(nums[i]);
			if (nums[i] < *median)
				median--;
			// Erase nums[i-k].
			if (nums[i - k] <= *median)
				median++;
			it=window.find(nums[i - k]);
			window.erase(it);
		}
		if (k % 2 == 1)
			res.push_back(*median);
		else {
			int prev = *(--median); median++;
			if (prev > 0 && *median > 0 || prev < 0 && *median < 0) {
				temp = *median*1.0 + (-*median + prev)*1.0 / 2;

			}
			else {
				temp = (*median + prev)*1.0 / 2;
			}
			res.push_back(temp);
		}
		return res;
	}
};
int main() {
	vector<double> nu;
	Solution s1 = Solution();
	int a = 2147483647;
	int b = 2147483647;
	cout << 1.0*(b + a) / 2;;
	vector<int> nums = { 1000000000, 0, 1 };
	multiset<int> window(nums.begin(), nums.end());
	multiset<int>::iterator it = window.begin();
	it++;
	window.insert(2);
	s1.medianSlidingWindow(nums, 2);
	system("pause");
	return 0;
}

本题难度较大
首先难点在于在O(1)时间内找到median
用一个multiset 这样可以接受元素数值相同，同时可以自动排序
关键点在于如何对median移动
if (nums[i] < *median)
	median--;
// Erase nums[i-k].
if (nums[i - k] <= *median)
	median++;
注意等号的位置
最后要注意
if (prev > 0 && *median > 0 || prev < 0 && *median < 0) {
	temp = *median*1.0 + (-*median + prev)*1.0 / 2;
}
else {
	temp = (*median + prev)*1.0 / 2;
}
2147483647+2147483647/2
或者2147483647+(-2147483648)会溢出
最后编译器的不同可能会导致
*median*1.0 与1.0* *median的结果不同 因为从左往右的编译顺序和从右往左的编译顺序