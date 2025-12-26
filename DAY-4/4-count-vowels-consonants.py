#Q4 Function to count vowels and consonants

#function for finding vowels and consonants
def vowels_consonants(str):
    vowels = []
    consonants = []
    for i in str:
        if i.isalpha():
            if i in "aeiouAEIOU":
                if i not in vowels: #to avoid duplicates
                    vowels.append(i)
            else:
                if i not in consonants: #to avoid duplicates
                    consonants.append(i)
    return vowels,consonants

#taking input of string
string = str(input("Enter the word: "))

#storing and printing the result
list1 = vowels_consonants(string)
print("vowels:",list1[0],"consonants:",list1[1])