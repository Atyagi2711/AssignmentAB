# # (1) Write a Python function to find the maximum of three numbers
#
# def find_maximum(a, b, c):
#     return max(a, b, c)
#
# # Example usage
# num1 = 10
# num2 = 200
# num3 = 15
#
# result = find_maximum(num1, num2, num3)
# print("The maximum number is:", result)


# # (2). Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


# from functools import reduce
#
# # Sample List
# sample_list = [8, 2, 3, -1, 7]
#
# # Using lambda and reduce to multiply all numbers in the list
# result = reduce(lambda x, y: x * y, sample_list)
#
# print(result)


# # (3) Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


# def reverse_string(s):
#     return s[::-1]
#
# # Sample String
# sample_string = "1234abcd"
# print(reverse_string(sample_string))  # Expected Output: "dcba4321"

## Notes - In this program, the reverse_string function takes a string s and returns it reversed using slicing (s[::-1]). The slicing operation [::-1] effectively reverses the string.


# # (4) Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# # Example usage
# number = 10
# print(f"The factorial of {number} is {factorial(number)}")

##Notes - In this function, factorial is defined recursively:
##If n is 0, it returns 1 (since the factorial of 0 is 1).
##Otherwise, it returns n multiplied by the factorial of n-1.


# # (5). Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# #Sample List :[1,2,3,3,3,3,4,5]
# #Unique List :[1, 2, 3, 4, 5]


# def unique_elements(input_list):
#     # Using set to remove duplicates and then converting back to list
#     return list(set(input_list))
#
# # Sample List
# sample_list = [4, 3, 2, 1, 8, 7, 5]
# # Unique List
# unique_list = unique_elements(sample_list)
# print("Unique List:", unique_list)

## NOTES - hen you run this code with the sample list [1, 2, 3, 3, 3, 3, 4, 5], it will output:
## Unique List: [1, 2, 3, 4, 5]


## (6). Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
##Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.


# def is_prime(number):
#     # Check if number is less than or equal to 1
#     if number <= 1:
#         return False
#     # Check for 2 and 3
#     if number <= 3:
#         return True
#     # Eliminate multiples of 2 and 3
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#     # Check for remaining numbers
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
# # Example usage
# num = 31
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

##  NOTES - This method eliminates multiples of 2 and 3 early on and then checks for factors from 5 onwards, skipping even numbers and multiples of 3. When you run this code with the example number 29, it will output


## (7). Write a Python program to print the even numbers from a given list.
##Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
##Expected Result: [2, 4, 6, 8]


# def get_even_numbers(input_list):
#     # Using list comprehension to filter even numbers
#     return [num for num in input_list if num % 2 == 0]
#
# # Sample List
# sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 12]
# # Get even numbers
# even_numbers = get_even_numbers(sample_list)
# print("Even Numbers:", even_numbers)


## (8). Write a Python function that accepts a string and counts the number of upper and lower case letters.
##Sample String: 'The quick Brow Fox'
##Expected Output:
##No. of Upper case characters : 3
##No. of Lower case Characters : 12


# def count_upper_lower(input_string):
#     upper_count = 0
#     lower_count = 0
#     for char in input_string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#     return upper_count, lower_count
#
# # Sample String
# sample_string = 'The quick Brow Fox'
# # Count upper and lower case characters
# upper_case_count, lower_case_count = count_upper_lower(sample_string)
# print("No. of Upper case characters:", upper_case_count)
# print("No. of Lower case characters:", lower_case_count)


## (9). Write a Python function to sum all the numbers in a list.
##Sample List: (8, 2, 3, 0, 7)
##Expected Output: 20


# def sum_of_list(numbers):
#     return sum(numbers)
#
# # Sample List
# sample_list = [8, 2, 3, 0, 7, 8, 9]
# # Sum of all numbers in the list
# total_sum = sum_of_list(sample_list)
# print("Sum of all numbers:", total_sum)


## (10). Write a Python function that checks whether a passed string is a palindrome or not.
##Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses


# def is_palindrome(s):
#     # Remove spaces and convert to lowercase for uniformity
#     s = s.replace(" ", "").lower()
#     # Check if the string reads the same forward and backward
#     return s == s[::-1]
#
# # Example usage
# print(is_palindrome("madam"))  # Output: True
# print(is_palindrome("nurses run"))  # Output: True
# print(is_palindrome("hello"))  # Output: False

## NOTES - This function first removes any spaces and converts the string to lowercase to ensure the comparison is case-insensitive and ignores spaces. Then, it checks if the string is equal to its reverse.