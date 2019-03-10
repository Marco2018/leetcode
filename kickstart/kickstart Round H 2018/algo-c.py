import math
input_file=open("test-c.txt","r")
#input_file=open("C-small-attempt1.in","r")
output_file=open("out-c2.txt","w")
times=int(input_file.readline())
print(times)
for time in range(times):
    print(time)
    nums=[int(x) for x in input_file.readline().split()]
    n,m=nums[0],nums[1]
    nums=[0 for i in range(n+1)]
    if time==65:
        a=1
    for i in range(m+1):
        number=2**i*math.factorial(2*n-i)
        c=1
        for j in range(i):
           c=int(c*(m-j)/(j+1))
        nums[i]=c*number%1000000007
    res=0
    for i in range(m+1):
        res+=(-1)**i*nums[i]
    res%=1000000007
    output_file.write("Case #"+str(time+1)+": ")
    output_file.write(str(res)+"\n")