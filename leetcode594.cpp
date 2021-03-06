#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> freqs;
        for (int n : nums) {
            freqs[n]++;
        }

        int longest = 0;
        int lastNum = 0;
        int lastFreq = 0;
        for (pair<int, int> p : freqs) {
            int freq2 = 0;
            if (lastFreq && p.first == lastNum + 1) {
                freq2 = p.second + lastFreq;
            }
            longest = max(longest, freq2);
            lastNum = p.first;
            lastFreq = p.second;
        }
        return longest;
    }
};
