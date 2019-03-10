#include<iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;
class Solution {
public:
	int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
		unordered_map<int, vector<int>> path;
		for (int i = 0; i < routes.size(); i++) {
			for (int j = 0; j < routes[i].size(); j++) {
				path[routes[i][j]].push_back(i);
			}
		}
		unordered_set<int> node_seen{S}, route_seen{};
		vector<int> travel{ S };
		int step = 0;
		while (travel.size()) {
			vector<int> new_nodes;
			for (int i = 0; i < travel.size(); i++) {
				int bus_stop = travel[i];
				if (bus_stop == T) {
					return step;
				}
				for (int j = 0; j < path[bus_stop].size(); j++) {
					int route = path[bus_stop][j];
					if (!route_seen.count(route)) {
						route_seen.insert(route);
						for (int k = 0; k < routes[route].size(); k++) {
							if (!node_seen.count(routes[route][k])) {
								node_seen.insert(routes[route][k]);
								new_nodes.push_back(routes[route][k]);
							}
						}
					}
				}
			}
			step++;
			travel = new_nodes;
		}
		return -1;
	}
};
int main() {
	Solution s1;
	int nums[2][3] = { {1,2,7},{3,6,7}};
	int nums2[6] = { 1,1,1,1,1,1 };
	vector <int> a;
	a.assign(nums2, nums2 + 6);

	vector<vector<int> > num(2);
	for (int i = 0; i < 2; i++) {
		num[i].assign(nums[i], nums[i] + 3);
	}
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 3; j++) {
			cout << num[i][j];
		}
	}
	//num.assign(nums, nums + 6);
	int S = 1, T = 1;
	int res;
	res=s1.numBusesToDestination(num, S, T);
	cout << res;
	system("pause");
	return 0;
}

#熟悉 vector set map等数据结构的用法
注意记录已经见过的route否则TLE