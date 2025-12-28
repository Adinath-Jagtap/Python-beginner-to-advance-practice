# Q5 Read CSV file and print rows

'''Without importing csv'''
with open("DAY-6/required files/data.csv", "r") as file:
    lines = file.readlines()

for line in lines[1:]: # skip header
    row = line.strip().split(",")
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")

print("___________________________________________________________________\n")

'''Importing CSV'''
import csv
with open("DAY-6/required files/data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # skip header

    for row in reader:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")