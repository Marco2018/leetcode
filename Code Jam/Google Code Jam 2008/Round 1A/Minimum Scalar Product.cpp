#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
double circle_segment(double rad, double th) {
	return rad * rad*(th - sin(th)) / 2;
}
int main() {
	//ifstream in("test.txt");
	//ifstream in("A-small-practice.in");
	ifstream in("A-large-practice.in");
	ofstream out("out.txt");
	int n, loop, i, j, t, temp;
	string line;
	getline(in, line);
	t = stoi(line);
	string str1;
	char* p;
	char line_cstr[100000];
	for (loop = 0; loop <t;loop++) {
		int res = 0;
		vector<int> veca_m, veca_p,vecb_m, vecb_p;
		getline(in, line);
		n = stoi(line);
		if (n == 0)return 0;
		getline(in, line);
		strcpy(line_cstr, line.c_str());
		p = strtok(line_cstr, " "); str1 = p;
		temp = stoi(str1);
		if (temp >= 0)
			veca_p.push_back(temp);
		else
			veca_m.push_back(temp);
		for (j = 1; j < n; j++) {
			p = strtok(NULL, " "); str1 = p; temp = stoi(str1);
			temp = stoi(str1);
			if (temp >= 0)
				veca_p.push_back(temp);
			else
				veca_m.push_back(temp);
		}
		getline(in, line);
		strcpy(line_cstr, line.c_str());
		p = strtok(line_cstr, " "); str1 = p;
		temp = stoi(str1);
		if (temp >= 0)
			vecb_p.push_back(temp);
		else
			vecb_m.push_back(temp);
		for (j = 1; j < n; j++) {
			p = strtok(NULL, " "); str1 = p; temp = stoi(str1);
			temp = stoi(str1);
			if (temp >= 0)
				vecb_p.push_back(temp);
			else
				vecb_m.push_back(temp);
		}
		sort(veca_m.begin(), veca_m.end());
		sort(veca_p.begin(), veca_p.end());
		sort(vecb_m.begin(), vecb_m.end());
		sort(vecb_p.begin(), vecb_p.end());
		//veca_m,vecb_p
		int m1,m2,m3,m4;
		m1 = veca_m.size(); m2 = veca_p.size();
		m3 = vecb_m.size(); m4 = vecb_p.size();
		if (m1 >= m4) {
			for (j = 0; j < m4; j++) {
				res += veca_m[j] * vecb_p[m4 - 1 - j];
			}
			for (j = 0; j < m2; j++) {
				res += vecb_m[j]* veca_p[m2-1-j];
			}
			for (j = 0; j < m1-m4; j++) {
				res += veca_m[m4+j] * vecb_m[m3-1-j];
			}
		}
		else {
			for (j = 0; j < m1; j++) {
				res += veca_m[j] * vecb_p[m4 - 1 - j];
			}
			for (j = 0; j < m3; j++) {
				res += vecb_m[j]* veca_p[m2-1-j];
			}
			for (j = 0; j < m2-m3; j++) {
				res += veca_p[j] * vecb_p[m2 - m3 - 1 -j];
			}
		}
		out << "Case #" << loop + 1 << ": " << res << endl;
	}
	system("pause");
	return 0;
}