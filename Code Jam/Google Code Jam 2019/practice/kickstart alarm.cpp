#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <cmath>
using namespace std;
int T;
typedef long long ll;
ll pow1(ll x, ll y, ll z) {
	ll t = 1;
	for (ll k = 0; k < y; k++) {
		t = (t*x) % z;
	}
	return t;
}
int main() {
	cin >> T;
	ll i,j,N,K,x1,y1,C,D,E1,E2,F,x2,y2,time;
	ll res;
	for (time = 0; time < T; time++) {
		res = 0;
		cin >> N >> K >> x1 >> y1 >> C >> D >> E1 >> E2 >> F;
		vector<ll>k_nums(N); 
		fill(k_nums.begin(), k_nums.end(), 0);
		vector<ll>A(N);
		fill(A.begin(), A.end(), 0);
		A[0] = (x1 + y1) % F;
		for (i = 1; i < N; i++) {
			x2 = (C*x1 + D * y1 + E1) % F;
			y2 = (D*x1 + C * y1 + E2) % F;
			A[i] = (x2 + y2) % F;
			x1 = x2; y1 = y2;
		}
		for (i = 0; i <N; i++) {
			for (j = 0; j < K; j++) {
				k_nums[i] += pow1(i + 1, j + 1, 1000000007);
				k_nums[i] %= 1000000007;
			}
		}
		ll sum_knums;
		for (i = 0; i < N; i++) {
			sum_knums = 0;
			for (j = 0; j <= i; j++) {
				sum_knums += k_nums[j];
			}
			res += A[i] * (N - i)*sum_knums;
			res %= 1000000007;
		}
		cout << "Case #" << time + 1 << ": " << res << endl;
	}
	return 0;
}