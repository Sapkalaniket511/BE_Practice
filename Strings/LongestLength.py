def Longestlength(string):
    words = [];
    string = string + " ";
    word = "";
    for i in range(0, len(string)):
        if (string[i] == ' '):
            words.append(word);
            word = "";
        else:
            word = word + string[i];
    large = words[0];
    for k in range(0, len(words)):
        if (len(large) < len(words[k])):
            large = words[k];
    print("Largest Length word: " + large);



sA=str(input("Enter the String="))
Longestlength(sA)
