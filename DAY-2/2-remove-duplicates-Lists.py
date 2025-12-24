# Q2 : Remove duplicates from list

#Take input of list
old_list = list(input("ENTER LIST INPUT: ").split(","))

#Creating new empty list
new_list = []

#For loop for appending non duplicate elements in new list
for i in old_list:
    if i in new_list:
        continue
    else:
        new_list.append(i)

#Printing the final new list (without duplicates)
print(new_list,"is a non duplicate elements version of list",old_list)