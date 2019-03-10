#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<sstream>
#include <typeinfo>
#include<map>
#include<bitset>
using namespace std;
class Solution {
public:
	vector<string> readBinaryWatch(int num) {
		vector<string> rs;
		for (int h = 0; h < 12; h++)
			for (int m = 0; m < 60; m++)
				if (bitset<10>(h << 6 | m).count() == num) {
					if (m<10)
						rs.push_back(to_string(h) + ":0" + to_string(m));
					else
						rs.push_back(to_string(h) + ":" + to_string(m));

				}
		return rs;
	}
};
int main() {
	Solution s1 = Solution();
	vector<string> res;
	res=s1.readBinaryWatch(1);
	for (int i = 0; i < res.size(); i++) {
		cout << res[i];
	}
	system("pause");
	return 0;
}