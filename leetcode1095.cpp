class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
       int n = A.length(), l, r, m, peak = 0;
       l = 0;
       r = n-1;
       while(l<r){
            m = (l+r)/2;
            if(A.get(m)<A.get(m+1)) l =peak = m+1;
            else r=m;
       }
        //find in left of the peak
        l = 0;
        r = peak;
         while (l <= r) {
            m = (l + r) / 2;
            if (A.get(m) < target)
                l = m + 1;
            else if (A.get(m) > target)
                r = m - 1;
            else
                return m;
        }
        // find target in the right of peak
        l = peak;
        r = n - 1;
        while (l <= r) {
            m = (l + r) / 2;
            if (A.get(m) > target)
                l = m + 1;
            else if (A.get(m) < target)
                r = m - 1;
            else
                return m;
        }
        return -1;
    }
};   