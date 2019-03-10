#include <iostream>
#include <array>
#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
	bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
		stack<int> s;
		int i, j=0;
		for (i = 0;i < pushed.size();i++) {
			s.push(pushed[i]);
			while (s.size() && s.top() == popped[j]) {
				s.pop();
				j += 1;
			}
		}
		if (j == popped.size())
			return true;
		return false;
	}
};
int main() {
	Solution s1;
	vector<int> pushed = { 1,2,3,4,5 };
	vector<int> popped = { 4,5,3,2,1 };
	int res=s1.validateStackSequences(pushed,popped);
	cout << res;
	system("pause");
	return 0;
}
// for this kind problem, simulate stack