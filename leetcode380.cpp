#include<iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;
class RandomizedSet {
public:
	/** Initialize your data structure here. */
	RandomizedSet() {
		
	}

	/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
	bool insert(int val) {
		if (map1.find(val) != map1.end()) return false;
		nums.push_back(val);
		map1[val] = nums.size()-1;
		return true;
	}

	/** Removes a value from the set. Returns true if the set contained the specified element. */
	bool remove(int val) {
		if (map1.find(val) == map1.end()) return false;
		int index = map1[val];
		int temp;
		temp = nums[index];
		nums[index] = nums[nums.size() - 1];
		nums[nums.size() - 1] = temp;
		map1[nums[index]] = map1[val];
		map1.erase(val);
		nums.pop_back();
		return true;
	}

	/** Get a random element from the set. */
	int getRandom() {
		return nums[rand() % nums.size()];
	}
private:
	unordered_map<int, int> map1;
	vector<int> nums;
};
int main() {
	RandomizedSet s1;
	s1.insert(1);
	s1.insert(2);
	s1.insert(3);
	s1.remove(2);
	s1.remove(3);
	int a=s1.getRandom();
	int b = s1.getRandom();
	cout << a << " " << b;
	system("pause");
	return 0;
}