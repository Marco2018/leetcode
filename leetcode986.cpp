#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
using namespace std;
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
struct Interval {
	int start;
	int end;
	Interval() : start(0), end(0) {}
	Interval(int s, int e) : start(s), end(e) {}
	
};
class Solution {
public:
	int min(int a, int b) {
		if (a < b)
			return a;
		return b;
	}
	int max(int a, int b) {
		if (a > b)
			return a;
		return b;
	}
	vector<Interval> intervalIntersection(vector<Interval>& A, vector<Interval>& B) {
		int n = A.size(), m = B.size();
		int i = 0, j = 0;
		vector<Interval> res;
		while (i < n && j < m) {
			if ((A[i].start <= B[j].end) && (A[i].end >= B[j].start)) {
				int start1 = max(A[i].start, B[j].start);
				int end1 = min(A[i].end, B[j].end);
				Interval re = Interval(start1, end1);
				res.push_back(re);
				if (A[i].end < B[j].end) i++;
				else j++;
			}
			else {
				if (A[i].start > B[j].end) {
					j++;
				}
				else {
					i++;
				}
			}
		}
		return res;
	}
};
int main() {
	Solution s1;
	vector<Interval> A = { {Interval(0,2)},{Interval(5,10)} ,{Interval(13,23)} ,{Interval(24,25)} };
	vector<Interval> B = { {Interval(1,5)},{Interval(8,12)} ,{Interval(15,24)} ,{Interval(25,26)} };
	s1.intervalIntersection(A, B);
	return 0;
}