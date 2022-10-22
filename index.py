# QUESTION 1
"""
Write a function to print "hello_USERNAME!" USERNAME is the input 
of the function. The first line of the code has been defined as 
below.
"""
def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name("USERNAME")


# QUESTION 2
"""
Write a python function, first_odds that prints the odd numbers 
from 1-100 and returns nothing
"""
def first_odds():
    for i in range(1,101,2):
        print(i)


first_odds()


#QUESTION 3
"""
Please write a Python function, max_num_in_list to return the max 
number of a given list. The first line of the code has been defined as 
below.
"""
def max_num_in_list(a_list):
    return max(a_list)


favorite_nums = [8, 13, 19, 20, 52]
print("The maximum number is", max_num_in_list(favorite_nums))


# QUESTION 4
"""
Write a function to return if the given year is a leap year. A leap year 
is divisible by 4, but not divisible by 100, unless it is also divisible 
by 400. The return should be boolean Type (true/false).
"""
def is_leap_year(a_year):
    leap_year = False
    
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                leap_year = True
        else:
            leap_year = True
    return leap_year

user_year = int(input("Enter a year: "))
if is_leap_year(user_year):
    print(user_year, " is a leap year")

else:
    print(user_year, " is not a leap year")
	
	
# QUESTION 5
"""
Write a function to check to see if all numbers in list are consecutive numbers. 
For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not 
consecutive numbers. The return should be boolean Type.
"""
def is_consecutive(a_list):
    consecutive = False
    current_num = a_list[0]
    for i in a_list:
        if current_num == i:
            current_num += 1
            continue
        else:
            return consecutive
    consecutive = True
    return consecutive


my_list = [2,3,4,5,6,7]
my_other_list = [1,2,5]

print(is_consecutive(my_list))
print(is_consecutive(my_other_list))
