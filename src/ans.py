""" 
Practice Question 2: List Comprehension with Conditional

Task:

Create a function negative_to_zero that uses a list comprehension to 
convert all negative numbers in a list to 0 while keeping positive numbers unchanged.
"""

def negative_to_zero(input):
    return [0 if num < 0 else num for num in input]
