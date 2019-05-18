class Solution {
public:
    string getHint(string secret, string guess) {
        map<char,int> num;
        int i,n=secret.length(),a=0,b=0;
        for(i=0;i<n;i++){
            if(secret[i]==guess[i])
                a++;
            else{
                num[secret[i]]++;
            }
        }
        for(i=0;i<n;i++){
            if(secret[i]!=guess[i] && num[guess[i]]>0){
                b++;num[guess[i]]--;
            }
        }
        ostringstream oss;
        oss << a << "A" << b << "B";
        return oss.str();
    }
};

Runtime: 8 ms, faster than 76.13% of C++ online submissions for Bulls and Cows.
c++中map直接像当于defaultdict 都已经被初始化为0了
注意 map.count(key)函数返回的值0,1表示map中是否有key 
