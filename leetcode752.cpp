#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm> 
#include <string>
#include <queue>
#include <limits.h>
using namespace std;
struct point {
	int a;
	int b;
	int c;
	int d;
	point(int a, int b, int c, int d) :a(a), b(b), c(c), d(d) {}
};

class Solution {
public:
	int openLock(vector<string>& deadends, string target) {
		int dp[10][10][10][10];
		memset(dp, -1, sizeof(dp));
		point tar = point(target[0] - '0', target[1] - '0', target[2] - '0', target[3] - '0');
		queue<point> que;
		int a, b, c, d;
		int da[8] = { 1,-1,0,0,0,0,0,0 };
		int db[8] = { 0,0,1,-1,0,0,0,0 };
		int dc[8] = { 0,0,0,0,1,-1,0,0 };
		int dd[8] = { 0,0,0,0,0,0,1,-1 };
		int i, n = deadends.size();
		dp[0][0][0][0] = 0;
		for (i = 0; i < n; i++) {
			a = deadends[i][0] - '0';
			b = deadends[i][1] - '0';
			c = deadends[i][2] - '0';
			d = deadends[i][3] - '0';
			dp[a][b][c][d] = INT_MAX;
		}
		if (dp[0][0][0][0] != 0)return -1;
		que.push(point(0, 0, 0, 0));
		while (que.size()) {
			point tmp = que.front();
			que.pop();
			if (tmp.a == tar.a&&tmp.b == tar.b&&tmp.c == tar.c&&tmp.d == tar.d)
				break;
			for (i = 0; i < 8; i++) {
				int na = (tmp.a + da[i]) % 10, nb = (tmp.b + db[i]) % 10, nc = (tmp.c + dc[i]) % 10, nd = (tmp.d + dd[i]) % 10;
				if (na < 0) na += 10;
				if (nb < 0) nb += 10;
				if (nc < 0) nc += 10;
				if (nd < 0) nd += 10;
				if (dp[na][nb][nc][nd] == -1) {
					que.push(point(na, nb, nc, nd));
					dp[na][nb][nc][nd] = dp[tmp.a][tmp.b][tmp.c][tmp.d] + 1;
				}
			}
		}
		return dp[tar.a][tar.b][tar.c][tar.d];
	}
};
int main() {
	Solution s1;
	int nums[2][2] = {-1};
	memset(nums, -1, sizeof(nums));
	//fill(nums, nums + 2, -1);

	vector<string> deadends = { "0201", "0101","0102","1212","2002" };
	string target = "0202";
	//vector<string> deadends = { "8888"};
	//string target = "0009";
	//cout << 10 % 10;
	int res=s1.openLock(deadends, target);
	cout << res;
	system("pause");
	return 0;
};