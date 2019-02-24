#include <iostream>
#include <string>
#include <cassert>
using namespace std;
typedef long long ll;
int T;
int A, B, N;

int say(int x) {
	cout << x << endl;
	string S;
	cin >> S;
	if (S == "CORRECT")
		return 0;
	if (S == "TOO_BIG")
		return 1;
	if (S == "TOO_SMALL")
		return 2;
	else
		return 3;
}

int main() {
	cin >> T;
	for (auto k = 0; k < T; k++) {
		cin >> A >> B >> N;
		if (say(B) == 0)
			continue;
		int lb = A;
		int ub = B;
		while (ub - lb > 1) {
			bool flag = false;
			int t = (ub + lb) / 2;
			int a = say(t);
			assert(a < 3);
			if (a == 0) {
				flag = true;
			}
			else if (a == 1) {
				ub = t;
			}
			else {
				lb = t;
			}
			if (flag)
				break;
		}
	}
}