#Q6 Lambda function to sort list of tuples

#function for sorting
def sorting(n):
    sorted_data = sorted(n, key=lambda x: x[1])
    return sorted_data

#sample data
data = [(1, 3), (4, 1), (2, 2), (5, 0)]

#calling function and printing result
print(sorting(data),"is sorted list of given list of tuples")
