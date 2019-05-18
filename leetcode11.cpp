class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxarea=0,n=height.size(), i=0,j=height.size()-1,area;
        while(i<j){
            area=min(height[i],height[j])*(j-i);
            maxarea=max(area,maxarea);
            if(height[i]>height[j]) j--;
            else i++;
        }
        return maxarea;
    }
};

Runtime: 16 ms, faster than 98.32% of C++ online submissions for Container With Most Water.