def reverse(x):
    n=len(str(x))
    if x<0:
        y=-1*int(str(-x)[n-1::-1])
    else:
        y=int(str(x)[n-1::-1])
    if y>2**31-1 or y<-2**31:
        y=0
    return y

nums = 123
print(reverse(nums))
