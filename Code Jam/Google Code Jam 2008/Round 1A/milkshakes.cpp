#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int malt, unmalt;
bool issatis(vector <pair<int, int>>& customer, vector<int>& milk) {
	int i;
	for (i = 0; i < customer.size(); i++) {
		if (customer[i].second == milk[customer[i].first-1])
			return true;
	}
	int k;
	malt = unmalt = 0;
	for (k = 0; k < customer.size(); k++) {
		if (customer[k].second == 0)
			unmalt++;
		else
			malt++;
	}
	return false;
}
int main() {
	//ifstream in("test.txt");
	//ifstream in("B-small-practice.in");
	ifstream in("B-large-practice.in");
	ofstream out("out.txt");
	int n, loop, i, j, m,c, t,temp;
	string line;
	getline(in, line);
	c = stoi(line);
	string str1;
	char* p;
	char line_cstr[1000000];
	for (loop = 0; loop < c; loop++) {

		getline(in, line);
		n = stoi(line);
		getline(in, line);
		m = stoi(line);
		vector<vector <pair<int, int>> > customers(m);
		for (i = 0; i < m; i++) {
			getline(in, line);
			strcpy(line_cstr, line.c_str());

			p = strtok(line_cstr, " "); str1 = p;
			t = stoi(str1);
			int x, y;
			for (j = 0; j < t; j++) {
				p = strtok(NULL, " "); str1 = p; x = stoi(str1);
				p = strtok(NULL, " "); str1 = p; y = stoi(str1);
				customers[i].push_back(make_pair(x, y));
			}
		}
		bool flag, isbreak = true,impossible=false;
		vector<int> milkshake(n, 0);
		vector<vector <pair<int, int>> >::iterator it = customers.begin();
		while (!impossible) {
			for (it = customers.begin(); it != customers.end(); it++) {
				flag = issatis(*it, milkshake);
				if (flag)
					continue;
				int k;
				isbreak = false;
				if (malt == 0) {
					impossible = true;
					break;
				}
				if (malt == 1) {
					for (k = 0; k < (*it).size(); k++) {
						if ((*it)[k].second == 1)
							milkshake[(*it)[k].first-1] = 1;
					}
				}
			}
			if (isbreak)
				break;
			isbreak = true;
		}
		if (impossible) {
			out << "Case #" << loop + 1 << ": "<< "IMPOSSIBLE" << endl;
			continue;
		}
		out << "Case #" << loop + 1 << ":";
		for (int k = 0; k < milkshake.size(); k++) {
			out << " " << milkshake[k];
		}
		out << endl;
	}
	system("pause");
	return 0;
}

/*
感想：
使用贪心算法
搜索每个customer是否满意
如果不满意判断malt为1 
如果是1的话表示这种milkshake肯定要变成malt
如果不满意，且该顾客的偏好全都是unmalt则这种情况是impossible

但是这个贪心算法是有问题的
如果有两个customer 不满意 而且都malt=2 这样的话要对每一种milkshake 要不要变成malt投票 选择投票最多的那个
*/