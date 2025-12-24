#Q6 Create dictionary from two lists (keys and values)

#Input both lists from user 
keys = list(input("Enter List 1: ").split(","))
values = list(input("Enter List 2: ").split(","))

#combine and create a dictionary
person = dict(zip(keys,values))
#alternative method is to have a for loop and appending pair of key and value 

#printing result
print(person)