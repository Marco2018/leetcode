class Solution {
public:
    bool cansplit(vector<int>& nums, int m, int sum1){
        long long n = nums.size(), i = 0, temp = 0, k = 1;
        while(i < n){
            temp += nums[i];
            if(temp<=sum1) i++;
            else{
                temp = 0; k++;
            }
        }
        if(k<=m) return true;
        return false;
    }
    int splitArray(vector<int>& nums, int m) {
        long long left = 0, right = 0, mid;
        for(auto num: nums){
            left = max(left, (long long)num);
            right += num;
        }
        while (left< right){
            mid = (left+right)/2;
            if(cansplit(nums, m, mid)){
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return left;
    }
};  