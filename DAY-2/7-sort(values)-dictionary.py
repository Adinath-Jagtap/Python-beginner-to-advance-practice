#Q7 Sort dictionary by values

#sample data
scores = {"Alice": 85, "Bob": 92, "Charlie": 78,"Adinath": 98}

#sorting the dictionary using  values 
'''sorted_dictionary = dict(sorted(scores.items()))''' #sorting by keys
sorted_dictionary = dict(sorted(scores.items(),key=lambda x: x[1])) #sorting by values

#printing the results
print(sorted_dictionary)