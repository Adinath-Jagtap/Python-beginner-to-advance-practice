#Vowel Calculator 

#input of string and vowel count init 0
string = str(input("Enter the Word: "))
count = 0

for char in string:
    if char in "aeiouAEIOU":
        count +=1

print("Number of Vowels in the string:"+ string +" is : ",count)