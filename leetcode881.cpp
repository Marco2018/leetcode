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
	int numRescueBoats(vector<int>& people, int limit) {
		sort(people.begin(), people.end(), greater<int>());
		int res = 0;
		for (int i = 0; i < people.size(); i++) {
			res++;
			if (limit - people[i] >= people[people.size() - 1])
				people.pop_back();
		}
		return res;
	}
};
int main() {
	Solution s1;
	vector<int> people = { 10,5,5,1 };
	auto pos = lower_bound(people.begin(), people.end(), 5, greater<int>());
	cout << *pos;
	people.erase(pos);
	
	int limit = 3;
	int res=s1.numRescueBoats(people, limit);
	cout << res;
	system("pause");
	return 0;
}