#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	//ifstream in("test.txt");
	//ifstream in("B-small-practice.in");
	ifstream in("B-large-practice.in");
	ofstream out("out.txt");
	int n,a,b,i,j,t,loop;
	string line;
	getline(in, line);
	n = stoi(line);
	string str1, str2;
	char* p;
	char line_cstr[1000];
	for (loop = 0; loop < n;loop++) {
		vector<int>ab_start, ab_arrive, ba_start, ba_arrive;
		getline(in, line);
		t = stoi(line);
		getline(in, line);
		strcpy(line_cstr,line.c_str());
		p = strtok(line_cstr, " "); str1 = p;
		p = strtok(NULL, " "); str2 = p;
		a = stoi(str1); b = stoi(str2);
		for (i = 0; i < a; i++) {
			int temp;
			getline(in, line);
			str1 = line.substr(0, 5);
			str2 = line.substr(6, 11);
			temp = stoi(str1.substr(0, 2)) * 60 + stoi(str1.substr(3, 5));
			ab_start.push_back(temp);

			temp = stoi(str2.substr(0, 2)) * 60 + stoi(str2.substr(3, 5));
			ab_arrive.push_back(temp);
		}
		for (i = 0; i < b; i++) {
			int temp;
			getline(in, line);
			str1 = line.substr(0, 5);
			str2 = line.substr(6, 11);
			temp = stoi(str1.substr(0, 2)) * 60 + stoi(str1.substr(3, 5));
			ba_start.push_back(temp);

			temp = stoi(str2.substr(0, 2)) * 60 + stoi(str2.substr(3, 5));
			ba_arrive.push_back(temp);
		}
		i = j = 0;
		int res1 = a, res2 = b;
		sort(ab_start.begin(), ab_start.end());
		sort(ab_arrive.begin(), ab_arrive.end());
		sort(ba_start.begin(), ba_start.end());
		sort(ba_arrive.begin(), ba_arrive.end());
		while (i < a&&j < b) {
			if (ab_start[i] >= ba_arrive[j] + t){
				res1--;
				i++; j++;
			}
			else {
				i++;
			}
		}
		i = j = 0;
		while (i < b&&j < a) {
			if (ba_start[i] >= ab_arrive[j] + t) {
				res2--;
				i++; j++;
			}
			else {
				i++;
			}
		}
		out << "Case #" << loop + 1 << ": " << res1<<" "<<res2 << endl;
	}
	system("pause");
	return 0;
}