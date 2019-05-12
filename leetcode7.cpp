class Solution {
public:
    int reverse(int x) {
        long long res=0;
        while (x){
            res=res*10+x%10;
            x/=10;
        }
        return (res<INT_MIN || res>INT_MAX) ? 0 : res;
    }
};

Runtime: 4 ms, faster than 98.83% of C++ online submissions for Reverse Integer.
Memory Usage: 8.3 MB, less than 97.47% of C++ online submissions for Reverse Integer

1. long long 
2. 注意负数的情况
x=-13，-13%10=-3，这种写法可以不用单独考虑负数


