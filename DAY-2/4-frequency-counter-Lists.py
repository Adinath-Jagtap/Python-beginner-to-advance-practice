#Q4 Count frequency of each element in list

#list input from user
list_og = list(input("Enter the list: ").split(","))

counted_list = []
#counting frequency each element
print("Frequency of each element: ") 
for i in list_og :
    if i in counted_list:
        continue
    else:
        print(i,":",list_og.count(i))
        counted_list.append(i)