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
���е�nums��С��2^32
0100
1110
0010
��һ�����е����ֶ�����2���õ�����0 res+=0
�������ֱ�Ϊ
010
111
001
�ڶ����������ִ���2 �õ�2��1  1��0 res+=2
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