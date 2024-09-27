#Operators in python - Exercise :
# (1). Write a Program to find Maximum of 3 Numbers .

# a = int(input("Enter First Number:"))
# b = int(input("Enter Second Number:"))
# c = int(input("Enter Third Number:"))
#
# # Determine the maximum number using conditional expressions
# max_value = a if a > b and a > c else b if b > c else c
#
# print("Maximum Value:", max_value)

#Flow Control - Exercise
# (1). Write a Program to find Biggest of given 2 Numbers from the Key Board?

# # Input two numbers from the user
# n1 = int(input("Enter First Number:"))
# n2 = int(input("Enter Second Number:"))
#
# # Check which number is larger and print the result
# if n1 > n2:
#     print("Biggest Number is:", n1)
# else:
#     print("Biggest Number is:", n2)

# (2). Write a Program to Check whether the given Number is in between 1 and 10?
# # Input a number from the user
# n = int(input("Enter Number:"))
#
# # Check if the number is between 1 and 10
# if n >= 1 and n <= 10:
#     print("The number", n, "is in between 1 to 10")
# else:
#     print("The number", n, "is not in between 1 to 10")



# Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
#
# Addition
# Subtraction
# Multiplication
# Division
# Modulus
# Display the results for each operation.

#ANSWER
# Input two numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# Perform operations
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"
# modulus = num1 % num2 if num2 != 0 else "Undefined (cannot calculate modulus by zero)"

# Display results
# print("\nResults:")
# print("Addition:", addition)
# print("Subtraction:", subtraction)
# print("Multiplication:", multiplication)
# print("Division:", division)
# print("Modulus:", modulus)


# Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.

#ANSWER

# Input a number from the user
# num = int(input("Enter a number: "))
#
# # Check if the number is even or odd using modulus operator
# if num % 2 == 0:
#     print("The number", num, "is even.")
# else:
#     print("The number", num, "is odd.")


# Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.

#ANSWER

# # Input a number from the user
# num = float(input("Enter a number: "))
#
# # Check if the number is positive, negative, or zero
# if num > 0:
#     print("The number", num, "is positive.")
# elif num < 0:
#     print("The number", num, "is negative.")
# else:
#     print("The number is zero.")


# Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:
#
# 90 and above: A
# 80 - 89: B
# 70 - 79: C
# 60 - 69: D
# Below 60: F

#ANSWER

# # Input the marks from the user
# marks = float(input("Enter the student's marks: "))
#
# # Determine the grade based on the grading scale
# if marks >= 90:
#     grade = 'A'
# elif marks >= 80:
#     grade = 'B'
# elif marks >= 70:
#     grade = 'C'
# elif marks >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
#
# # Display the grade
# print("The student's grade is:", grade)


# Question 5: Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.

#ANSWER

# # Create and write to the file
# with open("sample.txt", "w") as file:
#     file.write("Hello, this is a sample file.")
#
# # Read and display the content of the file
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print("File content:")
#     print(content)


#Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.

#ANSWER

# # Open and read the file
# try:
#     with open("data.txt", "r") as file:
#         content = file.read()
#
#     # Count the number of words
#     words = content.split()  # Split content into words
#     word_count = len(words)   # Count the number of words
#
#     # Display the word count
#     print("The number of words in the file is:", word_count)
#
# except FileNotFoundError:
#     print("The file 'data.txt' does not exist.")


# Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.

# #ANSWER
# for number in range(1, 11):
#     print(number)


#Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.

#ANSWER

# # Get the number from the user
# number = int(input("Enter a number: "))
#
# # Display the multiplication table
# print(f"Multiplication table for {number}:")
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")




