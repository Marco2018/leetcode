#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
using namespace std;
int main() {
	//ifstream in("test.txt");
	//ifstream in("A-small-practice.in");
	ifstream in("A-large-practice.in");
	ofstream out("out3.txt");
	int n,s,i,j,q,k,res;
	string line,query;
	getline(in, line);
	n = stoi(line);
	for (i = 0;i < n;i++) {
		map<string, int>map1;
		res = 0;
		getline(in, line);
		s = stoi(line);
		vector<int> nums(s, 0);
		int number_eng_canuse = s;
		for (j = 0;j < s;j++) {
			getline(in, line);
			map1[line]=j;
		}
		getline(in, line);q = stoi(line);
		for (k = 0;k < q;k++) {
			getline(in, query);
			if (nums[map1[query]] == 0) {
				number_eng_canuse--;
			}
			if (number_eng_canuse == 0) {
				res++;number_eng_canuse = s-1;
				fill(nums.begin(), nums.end(), 0);
			}
			nums[map1[query]]++;
		}
		out << "Case #" << i + 1 << ": " << res << endl;
	}
	system("pause");
	return 0;
}