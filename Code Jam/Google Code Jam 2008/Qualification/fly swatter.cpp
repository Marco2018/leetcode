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
	ifstream in("test.txt");
	//ifstream in("B-small-practice.in");
	//ifstream in("B-large-practice.in");
	ofstream out("out.txt");
	int n,loop,i,j;
	double f, R, t, r, g;
	string line;
	getline(in, line);
	n = stoi(line);
	string str1, str2,str3,str4,str5;
	char* p;
	char line_cstr[1000];
	for (loop = 0; loop < n;loop++) {
		getline(in, line);
		strcpy(line_cstr,line.c_str());
		p = strtok(line_cstr, " "); str1 = p;
		p = strtok(NULL, " "); str2 = p;
		p = strtok(NULL, " "); str3 = p;
		p = strtok(NULL, " "); str4 = p;
		p = strtok(NULL, " "); str5 = p;
		f = stod(str1); R = stod(str2); t = stod(str3); r = stod(str4); g = stod(str5);
		double x1, x2, y1, y2;
		double arr = 0.0,rad=R-t-f;
		for (x1 = r + f; x1 < R - t - f; x1 += g + 2 * r) {
			for (y1 = r + f; y1 < R - t - f; y1 += g + 2 * r) {
				x2 = x1 + g - 2 * f;
				y2 = y1 + g - 2 * f;
				if (x2 <= x1 || y2 <= y1)
					continue;
				if (x1*x1 + y1 * y1 >= rad * rad)
					continue;
				if (x2*x2 + y2 * y2 <= rad * rad)
					arr += (x2 - x1)*(y2 - y1);
				else if (x1*x1 + y2 * y2 >= rad * rad &&
					x2*x2 + y1 * y1 >= rad * rad) {
					// Only (x1,y1) inside circle.
					arr += circle_segment(rad, acos(x1 / rad) - asin(y1 / rad)) +
						(sqrt(rad*rad - x1 * x1) - y1) *
						(sqrt(rad*rad - y1 * y1) - x1) / 2;
				}
				else if (x1*x1 + y2 * y2 >= rad * rad) {
					// (x1,y1) and (x2,y1) inside circle.
					arr += circle_segment(rad, acos(x1 / rad) - acos(x2 / rad)) +
						(x2 - x1) * (sqrt(rad*rad - x1 * x1) - y1 +
							sqrt(rad*rad - x2 * x2) - y1) / 2;
				}
				else if (x2*x2 + y1 * y1 >= rad * rad) {
					// (x1,y1) and (x1,y2) inside circle.
					arr += circle_segment(rad, asin(y2 / rad) - asin(y1 / rad)) +
						(y2 - y1) * (sqrt(rad*rad - y1 * y1) - x1 +
							sqrt(rad*rad - y2 * y2) - x1) / 2;
				}
				else {
					// All except (x2,y2) inside circle.
					arr += circle_segment(rad, asin(y2 / rad) - acos(x2 / rad)) +
						(x2 - x1)*(y2 - y1) -
						(y2 - sqrt(rad*rad - x2 * x2)) *
						(x2 - sqrt(rad*rad - y2 * y2)) / 2;
				}
			}
		}
		printf("Case #%d: %.6lf\n", loop+1, 1.0 - arr / (3.1415926*R*R / 4));
	}
	system("pause");
	return 0;
}