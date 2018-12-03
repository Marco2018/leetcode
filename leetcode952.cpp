#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<sstream>
#include<unordered_map>
using namespace std;
class UnionFindSet {
public:
	UnionFindSet(int n) : _parent(n) {
		for (int i = 0; i<n; i++) {
			_parent[i] = i;
		}
	}

	void Union(int x, int y) {
		_parent[Find(x)] = _parent[Find(y)];
	}

	int Find(int x) {
		if (_parent[x] != x) {
			_parent[x] = Find(_parent[x]);
		}
		return _parent[x];
	}

private:
	vector<int> _parent;
};

class Solution {
public:
	int largestComponentSize(vector<int>& A) {
		int n = *max_element(A.begin(), A.end());
		UnionFindSet ufs(n + 1);
		for (int &a : A) {
			for (int k = 2; k <= sqrt(a); k++) {
				if (a % k == 0) {
					ufs.Union(a, k);
					ufs.Union(a, a / k);
				}
			}
		}

		unordered_map<int, int> mp;
		int ans = 1;
		for (int &a : A) {
			ans = max(ans, ++mp[ufs.Find(a)]);
		}
		return ans;
	}
};
int main() {
	Solution s1 = Solution();
	vector<int> nums = { 4,6,15,35 };
	int res;
	res= s1.largestComponentSize(nums);
	cout << res;
	system("pause");
	return 0;
}


/*
vector<int> id(20000,0);
vector<int> size1(20000, 0);
class Solution {
public:
int maxfactor(int a, int b) {
int temp;
while (b%a != 0) {
temp = b % a;
b = a;
a = temp;
}
return a;
}
int find(int x) {
if (id[x] == x) return x;
else return id[x] = find(id[x]);
}
void union1(int a, int b) {
int f_x = find(a), f_y = find(b);
if (f_x == f_y) return;
id[f_x] = f_y;
size1[f_y] += size1[f_x];
max_len = max(max_len, size1[f_y]);
}
int largestComponentSize(vector<int>& A) {
int n = A.size(),i,j;
int temp;

for (i = 0; i < n; i++) {
id[i] = i;
size1[i] = 1;
}
sort(A.begin(), A.end());
for (i = 0; i < n; i++) {
for (j = i+1; j < n; j++) {
temp = maxfactor(A[i], A[j]);
if (temp>1)
union1(i, j);
}
}
return max_len;
}
private:
int max_len = 1;
};
*/