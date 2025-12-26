#Q7 Calculate Area
#concept of finding area with default width when width is not entered

#function with default width
def area(length, width=1):
    return length * width

# printing and calling function 
print(area(5))        # width uses default value
print(area(5, 3))     # width overridden