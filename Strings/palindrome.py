def Palindrome(String):
    str=''
    temp=String
    for i in String:
        str=i+str
    if(temp==str):
        print(String,"is Palindrome")
    else:
        print(String,"is not Palindrome")




sA=str(input("Enter the String="))
Palindrome(sA)