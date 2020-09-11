def Substring(String,Substring):
    count=[]
    for i in range(0,len(String)):
        k=i
        flage=0
        for j in range(0,len(Substring)):
            if String[k]!=Substring[j]:
                flage=1
            if flage:
                break
            k=k+1
        if flage==0:
            count.append(i)

    print("Position=",str(count[0]))





sA=str(input("Enter the String="))
chA=str(input("Enter the substring="))
Substring(sA,chA)