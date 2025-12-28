# Q10 Handle multiple exceptions (FileNotFound, ValueError, etc.)

try:
    # Try opening a file
    with open("DAY-6/required files/number.txt", "r") as file:
        data = file.read()
    
    # Convert content to integer
    number = int(data)
    print("Number squared:", number ** 2)

except FileNotFoundError:
    print("Error: The file does not exist!")

except ValueError:
    print("Error: The file does not contain a valid integer!")

except Exception as e:  # catches all other exceptions
    print("Unexpected error:", e)