#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstdio>
using namespace std;
class Solution {
public:
	double radius;
	double x_center;
	double y_center;
	Solution(double radius, double x_center, double y_center) {
		this->radius = radius;
		this->x_center = x_center;
		this->y_center = y_center;
	}

	vector<double> randPoint() {
		double x;
		double y;

		do {
			x = (2 * ((double)rand() / RAND_MAX) - 1.0) * radius;
			y = (2 * ((double)rand() / RAND_MAX) - 1.0) * radius;
		} while (x * x + y * y > radius * radius);

		return { x_center + x, y_center + y };
	}
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj.randPoint();
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