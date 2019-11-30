class Solution {
public:
    string removeDuplicateLetters(string s) {
        string res = "0";
        unordered_map<char, int> m1;
        vector<int> visited(26, 0);
        for(char c : s){
            auto it = m1.find(c);
            if(it!=m1.end())
                m1[c]++;
            else m1[c] = 1;
        }
        for (char c : s) {
            m1[c]--;
            if (visited[c-'a']) continue;
            while (res.back()>c && m1[res.back()]>0) {
                visited[res.back()-'a'] = 0;
                res.pop_back();
            }
            res += c;
            visited[c-'a'] = 1;
        }
        return res.substr(1);
    }
}; 