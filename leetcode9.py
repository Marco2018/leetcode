def isPalindrome(x):
    isPal=1
    n=len(str(x))
    right=n-1
    left=0
    while left<right:
        if str(x)[left]!=str(x)[right]:
            isPal=0
            break
        else:
            left=left+1
            right=right-1
    return  isPal

nums = 10
print(isPalindrome(nums))