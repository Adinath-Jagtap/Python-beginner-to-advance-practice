#Q5 Find common elements between two lists

#Input both lists from user 
list1 = list(input("Enter List 1: ").split(","))
list2 = list(input("Enter List 2: ").split(","))

#Finding common elements 
common_elements_list=[]
for i in list1:
    if i in list2 :
        common_elements_list.append(i)

#printing the result
print(common_elements_list,"is list of common elements from",list1,"&",list2)