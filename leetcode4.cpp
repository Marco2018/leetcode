class Solution {
public:
    int findksmall(int k,vector<int>& nums1,int start1,vector<int>& nums2,int start2){
        int m=nums1.size(),n=nums2.size();
        if(m-start1<n-start2)
            return findksmall(k,nums2,start2,nums1,start1);
        if (n==start2)
            return nums1[start1+k-1];
        if (k==1)
            return min(nums1[start1],nums2[start2]);
        int range2,range1;
        range2=min(k/2,n-start2);
        range1=k-range2;
        int pivot1,pivot2;
        pivot1=nums1[start1+range1-1];
        pivot2=nums2[start2+range2-1];
        if(pivot1==pivot2)
            return pivot1;
        else if (pivot1<pivot2)
            return findksmall(k-range1,nums1,start1+range1,nums2,start2);
        else
            return findksmall(k-range2,nums1,start1,nums2,start2+range2);
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m,n,k;
        m=nums1.size();n=nums2.size();
        k=(m+n)/2+1;
        if((m+n)%2==0){
            int mid1,mid2;
            mid1=findksmall(k,nums1,0,nums2,0);
            mid2=findksmall(k-1,nums1,0,nums2,0);
            return 1.0*(mid1+mid2)/2;
        }
        else
            return 1.0*findksmall(k,nums1,0,nums2,0);
    }
};

Runtime: 20 ms, faster than 97.88% of C++ online submissions for Median of Two Sorted Arrays.
Memory Usage: 9.8 MB, less than 99.14% of C++ online submissions for Median of Two Sorted Arrays.