#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;
class Solution {
public:
	vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
		int all_evensum = 0, i, n, query;
		n = A.size();
		vector<int> res;
		query = queries.size();
		for (i = 0; i < n; i++) {
			if (A[i] % 2 == 0)
				all_evensum += A[i];
		}
		int index, num;
		for (i = 0; i < query; i++) {
			index = queries[i][1];
			num = queries[i][0];
			if (A[index] % 2 == 0)
				all_evensum -= A[index];
			A[index] += num;
			if (A[index] % 2 == 0)
				all_evensum += A[index];
			res.push_back(all_evensum);
		}
		return res;
	}
};
int main() {
	Solution s1;
	vector<int> A = { 1,2,3,4 };
	vector<vector<int>> query = { {1,0},{-3,1},{-4,0},{2,3} };
	s1.sumEvenAfterQueries(A, query);
	return 0;
}