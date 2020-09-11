def Occurrence(str1,chA):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict[chA])





sA=str(input("Enter the String="))
chA=str(input("Enter the character to find the occurrence="))
Occurrence(sA,chA)
