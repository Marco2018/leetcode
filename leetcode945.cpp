#include <iostream>
#include <array>
#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
	int minIncrementForUnique(vector<int>& A) {
		int count = 0, prev = -1,temp;
		sort(A.begin(), A.end());
		for (int i = 0;i < A.size();i++) {
			temp = max(prev + 1, A[i]);
			count += temp-A[i];
			prev = temp;
		}
		return count;
	}
};
int main() {
	Solution s1;
	vector<int> nums = {3,2,1,2,1,7};
	int res=s1.minIncrementForUnique(nums);
	cout << res;
	system("pause");
	return 0;
}
/*
class Solution {
public:
	int minIncrementForUnique(vector<int>& A) {
		unordered_map<int, int> map1;
		int count = 0;
		for (int i = 0;i < A.size();i++) {
			if (map1.find(A[i]) == map1.end()) map1[A[i]] = 1;
			else {
				int temp = 1;
				while (map1.find(A[i] + temp) != map1.end())
					temp++;
				map1[A[i] + temp] = 1;
				count += temp;
			}
		}
		return count;
	}
};
*/