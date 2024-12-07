 # 15days.py
# prime numbers1,50

'''
#day1
# 1 Write a Python program to print "Hello, World!"
print("hello world") 

#1.1 Calculate the sum of two numbers entered by the user.
n1 = int(input("num1 : "))
n2 = int(input("num2 : "))
n3 = n1 + n2
print(n3)

#1.2 Convert temperature from Celsius to Fahrenheit.
c = float(input("enter celsius"))
f = ( c * (9/5)) + 32
print(f)


#1.3 Write a Python program to calculate the area of a
rectangle given its length and width+

l = float(input("length"))
b = float(input("breadth"))
area  = l * b
print(area)


#2 Create a program that takes a user's name and age as
input and prints a greeting message+
name = input("name ")
age = int(input("age "))
print("hi " + name)


#3 Write a program to check if a number is even or odd+
num = int(input("enter a number "))
if num % 2 == 0:
    print("even")
else:
    print("odd")
    

# Given a list of numbers, find the maximum and minimum
values
li = [1, 2, 3, 4, 4, 8]
print(max(li))
print(min(li))


# Create a Python function to check if a given string is a
palindrome+
s = input("enter a string ")
if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")


# Calculate the compound interest for a given principal
amount, interest rate, and time period+

p = float(input("principal amount"))
r = float(input("rate of interest"))
t = float(input("time in years"))
c = p * (1 + r/100) ** t
print(c)
print(round(c, 2))


# 7 Write a program that converts a given number of days into years, weeks and days+

days = int(input("days "))
years = days // 365
weeks = (days % 365) // 7
days = (days % 365) % 7
print(f"{years} years {weeks} weeks {days} days")#
'''
'''

# 8 Given a list of integers, find the sum of all positive numbers+

li = [1, -2, 3, -4, 5]
a = [i for i in li if i > 0]
print(sum(a))

b = [i for i in li if i < 0]
print(sum(b))


#9 Create a program that takes a sentence as input and counts the number of words in it+
string = input("string ")
words = string.split(" ")
print(len(words))


#10  Implement a program that swaps the values of two variables.
a = 5
b = 4
print("Before swapping: ", a, b)
a, b = b, a
print("after swapping : ", a, b )

'''
