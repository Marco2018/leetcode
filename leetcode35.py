def searchInsert(nums, target):
    n=len(nums)
    posi=0
    for i in range(n):
        if target>nums[i]:
            posi=posi+1
        else:
            return posi
    return posi

digits=[1,3,5,6]
target=7
print(searchInsert(digits,target))