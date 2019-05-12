class Solution {
public:
    string convert(string s, int numRows) {
        if(s.size()<=1 || numRows<=1)
            return s;
        int n=2*numRows-2;
        string *str = new string[numRows];
        for(int i=0;i<s.size();i++){
            int j=i%n;
            if(j<numRows)
                str[j].push_back(s[i]);
            else{
                j-=numRows;
                str[numRows-2-j].push_back(s[i]);
            }
        }
        string res="";
        for(int i=0;i<numRows;i++){
            res+=str[i];    
        }
        return res;
    }
};

Runtime: 8 ms, faster than 99.81% of C++ online submissions for ZigZag Conversion.
Memory Usage: 12.7 MB, less than 99.36% of C++ online submissions for ZigZag Conversion.