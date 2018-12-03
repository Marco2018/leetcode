#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<sstream>
using namespace std;
class Solution {
public:
	vector<int> deckRevealedIncreasing(vector<int>& deck) {
		int n = deck.size();
		sort(deck.begin(), deck.end());
		vector<int> res(n, 0);
		int flag = 0,i=0,j=0;
		while (j< n) {
			if (res[i] == 0) {
				if (flag == 1) {
					i++; flag = 0;
				}
				else {
					res[i++] = deck[j++];
					flag = 1;
				}
			}
			else {
				i++;
			}
			i = i % n;
		}
		return res;
	}
};
int main() {
	Solution s1 = Solution();
	vector<int> nums = { 1,2 };
	vector<int> res;
	res= s1.deckRevealedIncreasing(nums);
	for (int i = 0; i < res.size(); i++) {
		cout << res[i];
	}
	system("pause");
	return 0;
}