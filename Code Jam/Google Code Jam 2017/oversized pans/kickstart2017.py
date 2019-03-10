input_file=open("A-large-practice.in","r")
output_file=open("out.txt","w")
times=int(input_file.readline())
print(times)
for time in range(times):
    line=input_file.readline()
    #print(line.split())
    string,size=line.split()[0],int(line.split()[1])
    n=len(string)
    b=[0 for i in range(n)]
    for i in range(n):
        if string[i]=="+":
            b[i]=1
    count,flag=0,False
    for i in range(n):
        if b[i]==0:
            count+=1
            if i+size<=n:
                for j in range(i,i+size,1):
                    b[j]=1-b[j]
            else:
                flag=True
                break
    if flag==False:
        output_file.write("Case #"+str(time+1)+": "+str(count)+"\n")
    else:
        output_file.write("Case #" + str(time + 1) + ": " + "IMPOSSIBLE"+"\n")
