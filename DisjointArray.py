def Disjoint(x,y):
    flag=0
    for i in x:
        for j in y:
            if i==j:
                flag=1
    if(flag==0):
        print("Arrays Are Disjoint")
    else:
        print("Arrays Are Not Disjoint")



iNo1=int(input("Enter the first Array Size="));
lArray1=[]
for i in range(0,iNo1):
    lArray1.append(int(input("Enter the second Array element=")))

iNo2=int(input("Enter the second Array Size="));
lArray2=[]
for i in range(0,iNo2):
    lArray2.append(int(input("Enter the second Array element=")))

Disjoint(lArray1,lArray2)