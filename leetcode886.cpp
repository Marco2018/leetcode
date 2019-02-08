#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm> 
#include <string>
using namespace std;
class Solution {
public:
	bool DFS(int source,int color) {
		bool res = true;
		nums[source] = color;
		for (int i = 0; i < no_samegroup[source].size(); i++) {
			if (nums[no_samegroup[source][i]] == color)
				return false;
			else if (nums[no_samegroup[source][i]] == 0) {
				res = res && DFS(no_samegroup[source][i], -color);
			}
		}
		return res;
	}
	bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
		if (dislikes.size() == 0)
			return true;
		no_samegroup.resize(N);
		nums.resize(N);
		for (int i = 0; i < dislikes.size(); i++) {
			no_samegroup[dislikes[i][0]-1].push_back(dislikes[i][1]-1);
			no_samegroup[dislikes[i][1]-1].push_back(dislikes[i][0]-1);
		}
		bool res;
		for (int j = 0; j < N; j++) {
			if (nums[j] == 0)
				res = DFS(j, 1);
			if (!res) return false;
		}
		return true;
	}
private:
	vector<int> nums;
	vector<vector<int>> no_samegroup;
};
int main() {
	Solution s1;
	int N = 5;
	vector<vector<int>> dislikes = { {1,2},{3,4},{4,5},{3,5} };
	s1.possibleBipartition(N,dislikes);
	system("pause");
	return 0;
}