
# Q1.  Create variables for storing a person's name, age, and average test score.


name = "John Doe"          
age = 25                   
average_test_score = 88.5  

print("Name:", name)
print("Age:", age)
print("Average Test Score:", average_test_score)


# Q2: Concatenate two strings and print the result.
string1 = "Hello, "
string2 = "world!"

result = string1 + string2

print(result)


#Q 3: Create a list of fruits and access elements using indexing.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

first_fruit = fruits[0]   
second_fruit = fruits[1]  
third_fruit = fruits[2]  

print("First fruit:", first_fruit)   
print("Second fruit:", second_fruit) 
print("Third fruit:", third_fruit)    


# 4 Given a list of numbers, find the sum and average.
numbers = [10, 20, 30, 40, 50]

total_sum = sum(numbers)

average = total_sum / len(numbers)

print("Sum:", total_sum)        
print("Average:", average)      

#5 Create a program that takes a temperature in Celsius and converts it to Kelvin


def celsius_to_kelvin(celsius):
    return celsius + 273.15


celsius = float(input("Enter temperature in Celsius: "))

kelvin = celsius_to_kelvin(celsius)

print(f"Temperature in Kelvin: {kelvin:.2f} K")

#6 Implement a program that checks if a given string is a palindrome


def is_palindrome(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]


input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#7 Create a function to reverse a given string


def reverse_string(s):
    return s[::-1]


input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

#8 Given a list of names, concatenate them into a single string separated by spaces


#9 Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)


import string


def is_pangram(s):
    alphabet_set = set(string.ascii_lowercase)
    
    input_set = set(s.lower())
    
    return alphabet_set.issubset(input_set)


input_string = input("Enter a string to check if it's a pangram: ")
if is_pangram(input_string):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")


#10 Calculate the area and circumference of a circle given its radius.

import math

radius = float(input('Enter radius of circle: '))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('Area = %0.4f.' % (area))
print('Circumference = %0.4f.' % (circumference))


#11 Implement a program that converts a given number of minutes into hours and minutes.


def convert_minutes_to_hours_and_minutes(total_minutes):
    hours = total_minutes // 60  
    minutes = total_minutes % 60   
    return hours, minutes

total_minutes = int(input('Enter the number of minutes: '))

hours, minutes = convert_minutes_to_hours_and_minutes(total_minutes)

print(f'{total_minutes} minutes is equal to {hours} hours and {minutes} minutes.')

#12 Create a function to count the number of vowels in a given string


def count_vowels(input_string):
    
    vowels = "aeiouAEIOU"
    count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char in vowels:
            count += 1  # Increment count if the character is a vowel
            
    return count


user_input = input("Enter a string: ")

vowel_count = count_vowels(user_input)

print(f'The number of vowels in the given string is: {vowel_count}')


#13  Write a program to check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")