#input_file=open("test.txt","r")
input_file=open("A-large-practice.in","r")
output_file=open("out.txt","w")
times=int(input_file.readline())
print(times)
for time in range(times):
    city = [0 for i in range(5001)]
    output_file.write("Case #"+str(time+1)+":")
    n=int(input_file.readline())
    nums=input_file.readline().split()
    for ii in range(n):
        start=int(nums[2*ii])
        end=int(nums[2*ii+1])
        for j in range(start,end+1,1):
            city[j]+=1
    check_times=int(input_file.readline())
    for i in range(check_times):
        check_city=int(input_file.readline())
        output_file.write(" "+str(city[check_city]))
    output_file.write("\n")
    input_file.readline()
