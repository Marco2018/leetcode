class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start=0,max_length=0;
		int n=s.size();
		unordered_map<char,int> map;
		unordered_map<char,int> ::iterator it;
		for (int i=0;i<n;i++){
			it=map.find(s[i]);
			if(it!=map.end()&&it->second>=start){
				start=map[s[i]]+1;
			}
			else
				max_length = max(max_length, i - start + 1);
			map[s[i]]=i;
		}
		return max_length;
    }
};