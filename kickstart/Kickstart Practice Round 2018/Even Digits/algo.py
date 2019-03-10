#input_file=open("test.txt","r")
input_file=open("A-small-practice.in","r")
output_file=open("out.txt","w")
times=int(input_file.readline())
print(times)
def isodd(nums):
    str_num=str(nums)
    for i in range(len(str_num)):
        if int(str_num[i])%2==1:
            return True
    return False
for time in range(times):
    output_file.write("Case #"+str(time+1)+": ")
    count,flag=0,1
    num=int(input_file.readline().rstrip("\n"))
    left=right=0
    while isodd(left+num):
        left+=1
    while isodd(num-right):
        right+=1
    temp=min(left,right)
    output_file.write(str(temp)+"\n")

