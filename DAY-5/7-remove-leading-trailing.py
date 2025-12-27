# Q7 Remove leading/trailing whitespace

text = input("Enter the text: ")
clean_text = text.strip() # removes space/whitespaces from both ends
left = text.lstrip()   # removes space/whitespaces from left end
right = text.rstrip()   # removes space/whitespaces from right end

#printing results
print(clean_text)
print(left)
print(right)