#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstdio>
using namespace std;
class Solution {
public:
	int totalHammingDistance(vector<int>& nums) {
		int n = nums.size();
		int res = 0;
		for (int i = 0; i < 32; ++i) {
			int cnt0 = 0;
			int cnt1 = 0;
			for (int j = 0; j < n; ++j) {
				if (((nums[j] >> i) & 1) == 1) {
					++cnt1;
				}
				else {
					++cnt0;
				}
			}

			res += (cnt1 * cnt0);
		}

		return res;
	}
};
/*
所有的nums都小于2^32
0100
1110
0010
第一次所有的数字都处以2，得到三个0 res+=0
三个数字变为
010
111
001
第二次所有数字处以2 得到2个1  1个0 res+=2
01
11
00
*/
int main() {
	Solution so;
	int num = 10;
	char str[100];
	_itoa_s(num, str, 2);
	printf("%s\n", str);
	system("pause");
	return 0;
}