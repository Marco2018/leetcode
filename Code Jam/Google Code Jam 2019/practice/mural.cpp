#include <iostream>
#include <string>
#include <cassert>
#include <vector>
using namespace std;
int T;
int main() {
	cin >> T;
	int i,n,j;
	for (i = 0; i < T; i++) {
		cin >> n;
		vector<int> num(n), sums(n+1);
		int res = 0;
		sums[0] = 0;
		string line;
		cin >> line;
		for (j = 0; j < n; j++) {
			num[j] = line[j] - '0';
			sums[j + 1] = sums[j] + num[j];
		}
		int number = (n + 1) / 2;
		for (j = 0; j + number <= n; j++) {
			if(sums[j + number] - sums[j]> res )
				res = sums[j + number] - sums[j];
		}
		cout << "Case #" << i + 1 << ": " << res << endl;
	}
	return 0;
}