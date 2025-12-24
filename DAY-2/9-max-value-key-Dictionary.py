#Q9 Find key with maximum value in dictionary

#sample data
scores = {"Alice": 85, "Bob": 92, "Charlie": 78,"Adinath": 98,"piyush":87,"prajwal":88}

#converting values from dictionary to a list
values=list(scores.values())
print(values)
keys = list(scores.keys()) 
print(keys)

#finding maximum value from values
max_value = max(values)
print(max_value)

#finding key for the max value 
for key, value in scores.items():
    if value == max_value:
        #printing result
        print("Key with maximum value:", key)
