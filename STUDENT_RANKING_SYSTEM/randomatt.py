# in_name = str(input("Enter the name of the user: "))
# in_rollno = int(input("Enter the roll number of the student: "))
# in_branch = str(input("Enter the branch of the student: "))

# def skills():
#     print("The skills are divided into four categories: Basic, Intermediate, Advanced")
#
# skills()
#
# for rows in csv:
#
# def intern:
#     if

# import csv
#
# # Open the X CSV file for reading and the new CSV file for writing
# with open('exams.csv', 'r') as x_file, open('new_file.csv', 'w', newline='') as new_file:
#
#     # Create CSV reader and writer objects
#     x_reader = csv.reader(x_file)
#     writer = csv.writer(new_file)
#
#     # Iterate through each row in the X CSV file
#     for row in x_reader:
#
#         # Check if the current row contains a file path
#         if 'branch' in row[0]:
#
#             # If it does, open the file and append its contents to the new CSV file
#             with open(row[0], 'r') as file:
#                 reader = csv.reader(file)
#                 for file_row in reader:
#                     writer.writerow(file_row)
# with open("temp.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# import csv
# import random
# # Open the CSV file in append mode
# with open('temp.csv', 'a', newline='') as csvfile:
#
#     # Create a csv.writer object
#     writer = csv.writer(csvfile, delimiter=',')
#
#     # Generate random data to be appended
#     column1 = [random.randint(1, 100) for i in range(5)]
#     column2 = [random.choice(['a', 'b', 'c']) for i in range(5)]
#     column3 = [random.randint(8, 15) for i in range(5)]
#
#     # Write the data to the CSV file
#     for i in range(len(column1)):
#         writer.writerow([column1[i], column2[i], column3[i]])

# import csv
#
# # Open the CSV file in read mode
# with open('temp.csv', 'r') as file:
#     # Create a CSV reader object
#     reader = csv.reader(file)
#
#     # Loop through each row in the CSV file and print it
#     for row in reader
#         print(row)

"""
import csv

# Open the CSV file in read mode
with open('temp.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Extract the second column into a list
    column_list = []
    check_list = []
    for row in reader:
        column_list.append(row[1])
    for check in column_list:
        if "25,55" == check:
            check_list.append(check)

    # Print the list containing the values of the second column
    print(column_list)
    print(check_list)
"""

"""
import random
import json

json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

values_list = ["blue", 45, "London", True, ["apple", "banana", "orange"]]

# Add random value from the list to the JSON
random_value = random.choice(values_list)
json_data["random_value"] = random_value

# Encode the JSON to a string
json_string = json.dumps(json_data)

# Print the encoded JSON string
print(json_string)
"""

# import csv
# import random
#
# # Open the CSV file in write mode
# with open('temp.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#
#     # Write the header row
#     writer.writerow(['Internships'])
#
#     # Generate and write random values for 10 rows
#     for i in range(100):
#         row = [random.randrange(1, 5)]
#         writer.writerow(row)


"""
import random
import csv

# Generate 10 random float values between 0 and 1
random_numbers =[round(random.uniform(2, 4.001), 3) for _ in range(100)]

# Open a CSV file for writing
with open('temp.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Faculty review'])

    # Write each random number to a new row in the CSV file
    for number in random_numbers:
        writer.writerow([number])
"""