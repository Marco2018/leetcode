#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<sstream>
#include <typeinfo>
#include<map>
#include<bitset>
#include<queue>
using namespace std;
class Solution {
public:
	vector<int> prisonAfterNDays(vector<int>& cells, int N) {
		int i,j;
		vector<int> temp(8, 0);
		map<vector<int>, int> map1;
		map<int, vector<int>> map2;
		for (i = 1; i <= N; i++) {		
			for (j = 1; j < 7; j++) {
				if (cells[j - 1] == cells[j + 1])
					temp[j] = 1;
				else
					temp[j] = 0;
			}
			temp[0] = temp[7] = 0;
			cells = temp;
			if (map1.count(cells) != 0) {
				int left;
				int loop = i-1;
				left = N % loop;
				if (left == 0) left = loop;
				return map2[left];
			}
			fill(temp.begin(),temp.end(), 0);
			map1[cells] = i;
			map2[i] = cells;
		}
		return cells;
	}
};
int main() {
	Solution s1 = Solution();
	vector<int> nums = {1,1,0,1,1,0,1,1};
	vector<int> res;
	int n = 1000000000;
	res=s1.prisonAfterNDays(nums,27);
	for (int i = 0; i < 8; i++) {
		cout << res[i];
	}
	system("pause");
	return 0;
}