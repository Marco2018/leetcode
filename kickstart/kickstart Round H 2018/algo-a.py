#input_file=open("test-a.txt","r")
input_file=open("A-large.in","r")
output_file=open("out_a_1.txt","w")
times=int(input_file.readline())
print(times)
for time in range(times):
    print(time)
    res=0
    nums=[int(x) for x in input_file.readline().split()]
    n,p,pres=nums[0],nums[1],[]
    res=2**n
    for i in range(p):
        line = input_file.readline().strip()
        index,j=1,0
        while j <len(pres):
            if len(pres[j])<= len(line) and line[:len(pres[j])]==pres[j]:
                index=0
                break
            if len(pres[j]) >= len(line) and pres[j][:len(line)] == line:
                pres.remove(pres[j])
                j-=1
            j+=1
        if index:
            pres.append(line)

    for i in range(len(pres)):
        length=len(pres[i])
        res-=2**(n-length)

    output_file.write("Case #"+str(time+1)+": ")
    output_file.write(str(res)+"\n")

