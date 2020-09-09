def Reverse(Array):
    RArray=[]
    for i in range(1,len(Array)+1):
        RArray.append(Array[len(Array)-i])
    return RArray
iNo=int(input());
lArray=[]
for i in range(0,iNo):
    lArray.append(int(input()))
print(Reverse(lArray))
