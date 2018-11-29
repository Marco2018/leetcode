#include <iostream>
#include <array>
#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
	int find(int x) {
		return id[x];
	}
	void union1(int x, int y, int n) {
		int xid = find(x);
		int yid = find(y);
		if (xid == yid) return;
		for (int i = 0;i <n;i++) {
			if (id[i]==xid) id[i]=yid;
		}
		islands--;
		return;
	}
	int removeStones(vector<vector<int>>& stones) {
		int i = 0,j;
		int n = stones.size();
		for (i = 0;i < n;i++) {
			id[i] = i;
		}
		islands = n;
		for (i = 0;i < n;i++) {
			for (j = i + 1;j < n;j++) {
				if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
					union1(i, j, n);
				}
			}
		}
		return n - islands;
	}
private:
	int id[1000];
	int islands = 0;
};
int main() {
	Solution s1;
	vector<vector <int> > num(5, vector<int>(2));
	int nums[5][2] = { {0,0},{0,2},{1,1},{2,0},{2,2} };
	for (int i = 0; i < 5; i++) {
		num[i].assign(nums[i], nums[i] + 2);
	}
	int res=s1.removeStones(num);
	cout << res;
	system("pause");
	return 0;
}
// for this kind problem, simulate stack