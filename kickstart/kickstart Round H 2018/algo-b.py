#input_file=open("test-b.txt","r")
input_file=open("B-large.in","r")
output_file=open("out.txt","w")
times=int(input_file.readline())
print(times)
for time in range(times):
    print(time)
    if time==4:
        a=1
    n=int(input_file.readline())
    num=int((n-1)/2)+1
    beauty=[0 for i in range(n)]
    beauty_str=input_file.readline().strip()
    for i in range(n):
        beauty[i]=ord(beauty_str[i])-ord("0")
    res=temp=sum(beauty[:num])
    for i in range(num,n,1):
        temp=temp+beauty[i]-beauty[i-num]
        res=max(res,temp)
    output_file.write("Case #"+str(time+1)+": ")
    output_file.write(str(res)+"\n")

