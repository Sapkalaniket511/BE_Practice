def Occurrence(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict)





sA=str(input("Enter the String="))

Occurrence(sA)
