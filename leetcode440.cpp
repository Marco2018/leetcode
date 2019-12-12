class Solution {
public:
    int between_nums(int n, long first, long last){
        int count = 0;
        while(first<=n){
            count += min((long)n+1, last) - first;
            first *= 10; last *= 10;
        }
        return count;
    }
    int findKthNumber(int n, int k) {
        int result = 1;
        k--;
        while(k>0){
            int count = between_nums(n, result, result+1);
            if(k >= count){
                k -= count;
                result++;
            }
            else{
                result *= 10;
                k--;
            }
        }
        return result;  
    }
};