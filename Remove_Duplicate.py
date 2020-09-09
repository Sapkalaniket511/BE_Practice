def Duplicate(duplicate):
    empty=[]
    for i in duplicate:
        if i not in empty:
            empty.append(i)
    return empty
iNo=int(input());
lArray=[]
for i in range(0,iNo):
    lArray.append(int(input()))
print("List before removing duplicate=" + str(lArray))
print("List after removing Duplicate="+ str(Duplicate(lArray)))