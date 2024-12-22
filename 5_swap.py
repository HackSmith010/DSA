# Swapping two numbers without using third variable

'''
Swapping two numbers is an easy task we usually take a temporary variable to swap them
but by using a temporary variable the space complexity is high and time complexity is also high
but in competitive programming we focus on how to reduce the complexities of the code 
so here we will see how to swap two numbers without using a temporary variable
'''

# General way of swapping two numbers using a third variable
'''
a = 5
b = 10
temp = a
a = b
b = temp
print("The value of a after swapping is: ",a)
print("The value of a after swapping is: ",b)
'''

# Swapping two numbers without using a third variable or by using bitwise operator

a = 7
b = 9
a = a^b
b = a^b
a = a^b
print("The value of a after swapping is: ",a)
print("The value of a after swapping is: ",b)