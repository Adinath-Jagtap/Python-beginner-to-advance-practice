# Q4. Create a generator that yields squares of numbers

#square generator function 
def square_generator(num):
    for i in range(1,num+1):
        '''return i*i'''   # runs function completely eg : gives all water at once
        yield i*i    # pauses function and continues later eg : gives water little by little

number = int(input("Enter the number: ")) #input
for square in square_generator(number): #for loop because results are stored in form of objects at a data address
    print(square) #printing results