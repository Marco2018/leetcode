#input_file=open("test.txt","r")
input_file=open("C-small-practice.in","r")
output_file=open("out.txt","w")
times=int(input_file.readline())
print(times)
for time in range(times):
    output_file.write("Case #"+str(time+1)+":")
    n=int(input_file.readline())
    cities=[]
    for i in range(n):
        city1=input_file.readline().rstrip('\n')
        city2=input_file.readline().rstrip('\n')
        cities.append([city1,city2])
    while len(cities)!=1:
        i=1
        while i<len(cities):
            if cities[i][0]==cities[0][-1]:
                cities[0]=cities[0]+cities[i]
                cities.pop(i)
            elif cities[i][-1]==cities[0][0]:
                cities[0]=cities[i]+cities[0]
                cities.pop(i)
            i+=1
    for i in range(n):
        output_file.write(" "+cities[0][2*i]+"-"+cities[0][2*i+1])
    output_file.write("\n")



