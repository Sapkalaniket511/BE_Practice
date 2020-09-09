def FindMax(x):
    new=[]
    while x:
        max=x[len(x)-1]
        for i in x:
            if i>max:
                max=i
        new.append(max)
        x.remove(max)
    return new[1]
iNo=int(input("Enter number of elements:"))
lmax=[]
for i in range(1,iNo+1):
    iNo1=int(input("Enter element:"))
    lmax.append(iNo1)
print("Second Largest Number Is=" + str(FindMax(lmax)))
