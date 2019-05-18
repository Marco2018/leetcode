class Solution {
public:
    int myAtoi(string str) {
        int sign = 1, i = 0 , n=str.length();
        long long result=0;
        while (i<n && str[i] == ' ') {i++;}
        if (i<n && str[i] == '-'){
            sign = -1;
            i++;
        }
        else if (i<n && str[i] == '+'){
            sign = 1;
            i++;
        }
        while (i<n && str[i] >= '0' && str[i] <= '9') {
            result  = 10 * result + (str[i++] - '0');
            if(result*sign >= INT_MAX) return INT_MAX;
            if(result*sign <= INT_MIN) return INT_MIN;
        }
        return result * sign;
    }
};

Runtime: 0 ms, faster than 100.00% of C++ online submissions for String to Integer (atoi).
