def Sum(Array):
    sum=0
    for i in range(0,len(Array)):
        sum=sum+Array[i]
    print("Sum of Array Element=",sum)
    print("Average of Array Element=",sum/len(Array))


iNo=int(input());
lArray=[]
for i in range(0,iNo):
    lArray.append(int(input()))
Sum(lArray)