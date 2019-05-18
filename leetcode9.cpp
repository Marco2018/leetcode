class Solution {
public:
    bool isPalindrome(int x) {
        int half=0;
        if (x<0 || x!=0 && x%10==0) return false;
        while (x>half){
            half=10*half+x%10;
            x/=10;
        }
        return x==half || x==half/10;
    }
};

c++编写这道题最大的问题在于其不知道x的长度，因此最好的方法就是就x的一半(half)
比较half和x的另一半是否相同
x==half x为偶数长
x==half/10 x为奇数长
Runtime: 8 ms, faster than 99.11% of C++ online submissions for Palindrome Number.