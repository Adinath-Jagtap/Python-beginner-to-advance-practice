#Q3 Merge two lists and sort the new list

#Taking input of both Lists
list1 = list(input("Enter List 1: ").split(","))
list2 = list(input("Enter List 2: ").split(","))

#Merging the list
merged_list = list1 + list2

#Sorting the combined list 
'''sorted_list = merged_list.sort()''' #does not create sort list instead sorts the existing one 
sorted_list = sorted(merged_list) #sorts and creats the new list in sorted_list variable

#Printing the results
print(sorted_list,"is sorted version of",merged_list,"which is merge list of ",list1,",",list2)