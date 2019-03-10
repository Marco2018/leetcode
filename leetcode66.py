def plusOne(digits):
    n=len(digits)
    nums=[0]*(n+1)
    carry=0
    for i in range(n):
        if i==0:
            nums[0]=digits[n-1]+1
            if nums[0]>=10:
                carry=1
                nums[0]=nums[0]-10
            continue
        nums[i]=digits[n-i-1]+carry
        if nums[i] >= 10:
            carry = 1
            nums[i] = nums[i] - 10
        else:
            carry=0
    nums[n]=carry
    nums.reverse()
    if carry==0:
        digits2=nums[1:n+1:1]
    else:
        digits2=nums[0:n+1:1]
    return digits2

digits=[8,9,9,9]
print(plusOne(digits))